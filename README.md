# XLSX to TSV Converter

The **xlsx_to_tsv.py** automates the conversion of all `.xlsx` files in a selected directory into `.tsv` format.

---

## Overview

This tool allows users to:
- **Batch Process Files:** Select a directory and convert all `.xlsx` files to `.tsv`.
- **Preserve Data Structure:** Ensures data integrity while converting files.
- **Save Output Automatically:** The converted `.tsv` files are saved in the same directory.

---

## Requirements

- **Python 3**
- **Libraries:**
  - `pandas`
  - `tkinter` (standard with Python)
  - `openpyxl` (Install via `pip install openpyxl`)

---


## Usage

1. Run the `xlsx_to_tsv.py` script.
2. A file dialog will prompt you to choose the folder containing the `.xlsx` files.
3. The script scans all `.xlsx` files in the selected directory, converts each of them into a `.tsv` format and saves them in the same directory with the `.tsv` extension.

---

## Important Notes

- **No Direct TSV Option in Excel:**  
  This script helps users bypass the lack of a direct "Save as TSV" feature in Excel and works for several files in a specified directory.

- **File Integrity:**  
  The script ensures that the data structure remains intact during conversion.

- **Large Files:**  
  Very large `.xlsx` files may require more processing time.

- **Backup Recommendation:**  
  Always keep a backup of your original Excel files before running the script.

---

## License

This project is available under the CC BY-NC 4.0 license. For complete details, please refer to the LICENSE file included with this project.
