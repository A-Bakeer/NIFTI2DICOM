"""
Example 2: Batch Convert Multiple NIfTI Files
==============================================

This example converts all .nii.gz files in a folder to separate DICOM series.
Each file gets its own subfolder.
"""

import sys
sys.path.insert(0, '..')

from nifti2dicom import nifti2dicom_mfiles

# Directory containing multiple .nii.gz files
nifti_folder = "data/patients/"

# Base output directory
output_base = "output/dicom_series/"

# Convert all files
nifti2dicom_mfiles(
    nifti_dir=nifti_folder,
    out_dir=output_base
)

print(f"All DICOM series saved under: {output_base}")
print("Folder structure:")
print("  output/dicom_series/patient_001_brain/slice0000.dcm")
print("  output/dicom_series/patient_002_liver/slice0000.dcm")
