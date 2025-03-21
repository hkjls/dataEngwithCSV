import pandas as pd
import tkinter as tk
from tkinter import filedialog

class extractor:
    def __init__(self):
        self._data = None
    
        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.askopenfilename(
            title="Select CSV file Source",
            filetypes=(("csv files", "*.csv"), ("all files", "*.*"))
        )
        
        if not self.file_path:
            raise ValueError("No file selected")

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, r) -> classmethod:
        if type(self.file_path) == str:
            data = pd.read_csv(self.file_path, sep=";", names = range(r))
            self._data = data