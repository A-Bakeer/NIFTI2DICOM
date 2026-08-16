"""
Example 1: Convert a Single NIfTI File to DICOM
================================================

This example shows how to convert one .nii.gz file into a DICOM series.
"""

import sys
sys.path.insert(0, '..')

from nifti2dicom import nifti2dicom_1file

# Path to your NIfTI file
nifti_file = "data/patient_001_brain.nii.gz"

# Output directory for DICOM slices
output_dir = "output/patient_001_dicom"

# Convert
nifti2dicom_1file(
    in_dir=nifti_file,
    out_dir=output_dir
)

print(f"DICOM series saved to: {output_dir}")
print("You should see files like: slice0000.dcm, slice0001.dcm, ...")
