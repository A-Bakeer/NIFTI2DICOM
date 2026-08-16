# NIfTI to DICOM Converter

A simple Python tool to convert NIfTI (`.nii.gz`) medical imaging files into DICOM (`.dcm`) series using SimpleITK.

## Features

- Convert single or multiple NIfTI files to DICOM format
- Preserves spatial orientation and slice positioning
- Generates deterministic DICOM UIDs to avoid duplicate series in viewers
- Supports batch processing of entire folders
- Maintains CT modality metadata for proper slice thickness handling

## Installation

### Prerequisites

- Python 3.7+

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/nifti2dicom.git
cd nifti2dicom

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Convert a Single NIfTI File

```python
from nifti2dicom import nifti2dicom_1file

nifti2dicom_1file(
    in_dir="path/to/brain.nii.gz",
    out_dir="path/to/output/dicom_series/"
)
```

### Convert Multiple NIfTI Files (Batch)

```python
from nifti2dicom import nifti2dicom_mfiles

nifti2dicom_mfiles(
    nifti_dir="path/to/nifti_files/",
    out_dir="path/to/output/"
)
```

Each `.nii.gz` file will get its own subfolder in the output directory.

## File Structure

```
nifti2dicom/
├── nifti2dicom.py      # Main conversion script
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── examples/           # Usage examples (optional)
```

## How It Works

1. **Reads** the NIfTI volume using SimpleITK
2. **Generates** deterministic DICOM UIDs based on the input file path (SHA-256 hash)
3. **Iterates** through each slice in the 3D volume
4. **Sets** DICOM metadata tags:
   - Series/Study Instance UIDs
   - Image Position (Patient) for 3D spacing
   - Image Orientation (Patient)
   - Instance Number
   - Modality (CT)
5. **Writes** each slice as an individual `.dcm` file

## DICOM Tags Set

| Tag | Description |
|-----|-------------|
| `0008\|0008` | Image Type (DERIVED\SECONDARY) |
| `0008\|0012` | Instance Creation Date |
| `0008\|0013` | Instance Creation Time |
| `0008\|0021` | Series Date |
| `0008\|0031` | Series Time |
| `0008\|0060` | Modality (CT) |
| `0008\|103e` | Series Description |
| `0020\|000d` | Study Instance UID |
| `0020\|000e` | Series Instance UID |
| `0020\|0013` | Instance Number (slice index) |
| `0020\|0032` | Image Position (Patient) |
| `0020\|0037` | Image Orientation (Patient) |

## Why Deterministic UIDs?

Using a hash of the input file path ensures:
- **Same file** → same UIDs (reproducible, no duplicates on re-run)
- **Different files** → different UIDs (proper separation in DICOM viewers)
- **No collisions** when processing multiple files in batch

## Dependencies

- [SimpleITK](https://simpleitk.org/) — Medical image I/O and processing

## License

MIT License — see [LICENSE](LICENSE) for details.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

Built with [SimpleITK](https://simpleitk.org/) and inspired by common medical imaging workflows.
