# examples/example_batch.py
"""
Example 2: Batch Convert Multiple NIfTI Files
==============================================

Converts all .nii.gz files in data/patients/ to separate DICOM series.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nifti2dicom import nifti2dicom_mfiles

nifti_folder = os.path.join("data", "patients")
output_base = os.path.join("output", "dicom_series")

nifti2dicom_mfiles(nifti_dir=nifti_folder, out_dir=output_base)

print(f"All DICOM series saved under: {output_base}")