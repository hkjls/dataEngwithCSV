import pandas as pd
import tkinter as tk
from tkinter import filedialog
from openpyxl import load_workbook

class extractor:
    def __init__(self):
        self._from_csv = None
        self._from_excel = None
    
        root = tk.Tk()
        root.withdraw()

    @property
    def from_csv(self):
        return self._from_csv
    
    @from_csv.setter
    def from_csv(self, r) -> classmethod:
        file_path = filedialog.askopenfilename(
            title="Select CSV file Source",
            filetypes=(("csv files", "*.csv"), ("all files", "*.*"))
        )
        
        if not file_path:
            raise ValueError("No file selected")
        
        if type(file_path) == str:
            data = pd.read_csv(file_path, sep=";", names = range(r))
            self._from_csv = data
            
    @property
    def from_excel(self):
        return self._from_excel
    
    @from_excel.setter
    def from_excel(self, sheet_name: str):
        file_path = filedialog.askopenfilename(
            title="Select CSV file Source",
            filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*"))
        )
        
        if not file_path:
            raise ValueError("No file selected")
        
        wb = load_workbook(file_path, data_only=True)
        ws = wb[sheet_name]
        self._from_excel = pd.DataFrame(ws.values)