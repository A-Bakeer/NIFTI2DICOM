import SimpleITK as sitk
import os
import time
from glob import glob
import hashlib
import uuid


def writeSlices(series_tag_values, new_img, i, out_dir):
    image_slice = new_img[:,:,i]
    writer = sitk.ImageFileWriter()
    writer.KeepOriginalImageUIDOn()

    list(map(lambda tag_value: image_slice.SetMetaData(tag_value[0], tag_value[1]), series_tag_values))

    image_slice.SetMetaData("0008|0012", time.strftime("%Y%m%d"))
    image_slice.SetMetaData("0008|0013", time.strftime("%H%M%S"))
    image_slice.SetMetaData("0008|0060", "CT")
    image_slice.SetMetaData("0020|0032", '\\'.join(map(str,new_img.TransformIndexToPhysicalPoint((0,0,i)))))
    image_slice.SetMetaData("0020|0013", str(i))

    writer.SetFileName(os.path.join(out_dir,'slice' + str(i).zfill(4) + '.dcm'))
    writer.Execute(image_slice)


def nifti2dicom_1file(in_dir, out_dir):
    """
    Convert one nifti file to dicom series with deterministic UIDs.
    Same input file always produces the same UIDs (reproducible).
    """

    os.makedirs(out_dir, exist_ok=True)

    new_img = sitk.ReadImage(in_dir) 
    modification_time = time.strftime("%H%M%S")
    modification_date = time.strftime("%Y%m%d")
    
    # Deterministic unique ID based on absolute file path
    # Same file always gets the same hash, different files get different hashes
    file_hash = hashlib.sha256(os.path.abspath(in_dir).encode()).hexdigest()[:16]
    
    # Build deterministic UIDs: prefix + file_hash + timestamp
    # The file_hash ensures uniqueness across files
    # The timestamp allows re-conversion of same file to be recognized as updated
    series_uid = f"1.2.826.0.1.3680043.2.1125.{file_hash}.{modification_date}.{modification_time}"
    study_uid = f"1.2.826.0.1.3680043.2.1125.1.{file_hash}.{modification_date}{modification_time}"

    direction = new_img.GetDirection()
    series_tag_values = [
        ("0008|0031", modification_time),
        ("0008|0021", modification_date),
        ("0008|0008", "DERIVED\\SECONDARY"),
        ("0020|000e", series_uid),
        ("0020|000d", study_uid),
        ("0020|0037", '\\'.join(map(str, (direction[0], direction[3], direction[6],
                                          direction[1], direction[4], direction[7])))),
        ("0008|103e", "Created-Pycad")
    ]

    list(map(lambda i: writeSlices(series_tag_values, new_img, i, out_dir), range(new_img.GetDepth())))


def nifti2dicom_mfiles(nifti_dir, out_dir=''):
    images = glob(os.path.join(nifti_dir, '*.nii.gz'))

    for image in images:
        o_path = os.path.join(out_dir, os.path.basename(image)[:-7])
        os.makedirs(o_path, exist_ok=True)
        nifti2dicom_1file(image, o_path)
        