import tkinter as tk
from tkinter import filedialog
import pandas as pd

def extractData():
    excel_filepath = filedialog.askopenfilename(
        title="Select Excel file",
        filetypes=[("Excel files", "*.xlsx;*.xls")]
    )
    
    params = pd.read_excel(excel_filepath, sheet_name="bloc type", engine="openpyxl", header=5)
    params = params[params.columns[1]]
    params = enumerate(params)
    param_obj = []
    for i, param in params:
        param_obj.append({
            "name": param,
            "ligne": i + 1,
            "colonne": 2
        })
    
    print(list(filter(lambda x: x["name"] == "DUREE BOURRAGE DEPILEUR", param_obj)))
    return

if __name__ == "__main__":
    extractData()