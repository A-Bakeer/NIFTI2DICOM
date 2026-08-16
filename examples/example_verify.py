"""
Example 4: Verify Converted DICOM Files
========================================

This example shows how to check that the DICOM files were created correctly.
"""

import os
from glob import glob

def verify_dicom_series(dicom_folder):
    """
    Basic verification of a DICOM series folder.
    """
    dcm_files = sorted(glob(os.path.join(dicom_folder, "*.dcm")))

    if not dcm_files:
        print(f"ERROR: No DICOM files found in {dicom_folder}")
        return False

    print(f"Found {len(dcm_files)} DICOM slice(s)")
    print(f"First slice: {os.path.basename(dcm_files[0])}")
    print(f"Last slice:  {os.path.basename(dcm_files[-1])}")

    # Check for consistent file sizes (basic integrity check)
    sizes = [os.path.getsize(f) for f in dcm_files]
    if len(set(sizes)) > 1:
        print("WARNING: Inconsistent file sizes detected")
    else:
        print(f"All slices have consistent size: {sizes[0]} bytes")

    return True

# Verify a converted series
if __name__ == "__main__":
    verify_dicom_series("output/patient_001_dicom")
