import pandas as pd
import os
from tkinter import Tk, filedialog

# Open a directory selection dialog
Tk().withdraw()  # Hide the root Tk window
directory = filedialog.askdirectory(title="Select a directory containing .xlsx files")

if directory:
    # Iterate over all .xlsx files in the selected directory
    for file_name in os.listdir(directory):
        if file_name.endswith(".xlsx"):
            file_path = os.path.join(directory, file_name)

            # Load the Excel file
            df = pd.read_excel(file_path, dtype=str)  # Ensure data is read as strings

            # Define the output .tsv file path
            tsv_file_path = os.path.join(directory, os.path.splitext(file_name)[0] + ".tsv")

            # Save as a TSV file (tab-separated, UTF-8 encoding)
            df.to_csv(tsv_file_path, sep='\t', index=False, encoding="utf-8")

            print(f"Converted: {file_name} → {os.path.basename(tsv_file_path)}")

    print("Conversion completed.")
else:
    print("No directory selected.")
