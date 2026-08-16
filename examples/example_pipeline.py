"""
Example 3: Integrate into a Pipeline
=====================================

This example shows how to use the converter as part of a larger workflow.
"""

import sys
import os
sys.path.insert(0, '..')

from nifti2dicom import nifti2dicom_1file
from glob import glob

def process_study(study_folder, output_root):
    """
    Process all NIfTI files from a study folder.
    Organizes output by patient ID.
    """
    nifti_files = glob(os.path.join(study_folder, "*.nii.gz"))

    for filepath in nifti_files:
        # Extract patient ID from filename
        filename = os.path.basename(filepath)
        patient_id = filename.split('_')[0]  # e.g., "sub-001" from "sub-001_T1w.nii.gz"

        # Create patient-specific output folder
        patient_output = os.path.join(output_root, patient_id, "dicom")
        os.makedirs(patient_output, exist_ok=True)

        print(f"Converting {filename} -> {patient_output}")
        nifti2dicom_1file(filepath, patient_output)

# Run the pipeline
if __name__ == "__main__":
    process_study(
        study_folder="data/neuro_study/",
        output_root="output/processed/"
    )
