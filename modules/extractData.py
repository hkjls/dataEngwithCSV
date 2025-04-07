import pandas as pd
import tkinter as tk
from tkinter import filedialog
from openpyxl import load_workbook

class extractor:
    def __init__(self):
        self._from_csv = None
        self._from_excel = None
        self._from_excel_pd = None
        
        self.excel_file_path = filedialog.askopenfilename(
            title="Select Excel file Source",
            filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*"))
        )
        self.csv_file_path = filedialog.askopenfilename(
            title="Select CSV file Source",
            filetypes=(("csv files", "*.csv"), ("all files", "*.*"))
        )
    
        root = tk.Tk()
        root.withdraw()

    @property
    def from_csv(self):
        return self._from_csv
    
    @from_csv.setter
    def from_csv(self, r):
        if type(self.csv_file_path) == str:
            data = pd.read_csv(self.csv_file_path, sep=";", header=r)
            self._from_csv = data
            
    @property
    def from_excel(self):
        return self._from_excel
    
    @from_excel.setter
    def from_excel(self, sheet_name: str):
        wb = load_workbook(self.excel_file_path, data_only=True)
        ws = wb[sheet_name]
        self._from_excel = pd.DataFrame(ws.values)
        
    @property
    def from_excel_pd(self):
        return self._from_excel_pd
    
    @from_excel_pd.setter
    def from_excel_pd(self, sheetname):        
        wb = pd.ExcelFile(self.excel_file_path)
        df = wb.parse(sheetname)
        self._from_excel_pd = df