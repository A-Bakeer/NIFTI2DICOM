"""
Example 1: Convert a Single NIfTI File to DICOM (with debugging)
================================================================
"""

import sys
import os

# Add parent directory (project root) to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nifti2dicom import nifti2dicom_1file

# Get the absolute path to the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Project root: {project_root}")
print(f"Current working directory: {os.getcwd()}")

# Build absolute path to the NIfTI file
nifti_file = os.path.join(project_root, "data", "patients", "hippocampus_001.nii.gz")
output_dir = os.path.join(project_root, "output", "hippocampus_001_dicom")

print(f"Looking for file: {nifti_file}")
print(f"File exists: {os.path.exists(nifti_file)}")

# List what's in the data folder
data_dir = os.path.join(project_root, "data", "patients")
print(f"\nContents of {data_dir}:")
if os.path.exists(data_dir):
    for f in os.listdir(data_dir):
        print(f"  - {f}")
else:
    print("  (folder does not exist)")

# Only proceed if file exists
if os.path.exists(nifti_file):
    nifti2dicom_1file(in_dir=nifti_file, out_dir=output_dir)
    print(f"\nDICOM series saved to: {output_dir}")
else:
    print(f"\nERROR: File not found: {nifti_file}")
    print("Please check that:")
    print("  1. You are running this script from the project root")
    print("  2. The file exists in data/patients/")
    print("  3. The filename matches exactly (case-sensitive)")
    
