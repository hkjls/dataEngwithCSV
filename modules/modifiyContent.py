import openpyxl
import tkinter as tk
from tkinter import filedialog

class ModifyContent:
    def __init__(self) -> None:
        
        root = tk.Tk()
        root.withdraw()
        self._filename = filedialog.askopenfilename(
            title="Select the file",
            filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*"))
        )
        self._wb = None
        self._ws = None
        
    def clearContent(self, sheetName: str, rows_range: int = 0, cols_range: int = 0) -> None:
        if type(self._filename) != str:
            raise ValueError("No file selected")
        
        if type(sheetName) != str:
            raise ValueError("No sheet Error")
        
        
        self._wb = openpyxl.load_workbook(self._filename)
        self._ws = self._wb[sheetName]
        
        
        if type(rows_range) == int and rows_range > 0:
            self._ws.delete_rows(6, rows_range)
            print('rows deleted')
        
        if type(cols_range) == int and cols_range > 0:
            self._ws.delete_cols(6, cols_range)
            
        self._wb.save(self._filename)
        