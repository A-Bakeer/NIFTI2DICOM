# examples/example_pipeline.py
"""
Example 3: Integrate into a Pipeline
=====================================

Process all NIfTI files from a study folder, organized by patient ID.
"""

import sys
import os
from glob import glob

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nifti2dicom import nifti2dicom_1file


def process_study(study_folder="data", output_root="output"):
    """
    Process all NIfTI files from a study folder.
    Organizes output by patient ID extracted from filename.
    """
    nifti_files = glob(os.path.join(study_folder, "*.nii.gz"))
    
    if not nifti_files:
        print(f"No .nii.gz files found in {study_folder}")
        return
    
    for filepath in nifti_files:
        filename = os.path.basename(filepath)
        patient_id = filename.split("_")[0]
        
        patient_output = os.path.join(output_root, patient_id, "dicom")
        os.makedirs(patient_output, exist_ok=True)
        
        print(f"Converting {filename} -> {patient_output}")
        nifti2dicom_1file(filepath, patient_output)


if __name__ == "__main__":
    process_study()