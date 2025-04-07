from tkinter import filedialog
import pandas as pd

class params:
    def __init__(self, file_path: str):
        self.PARAMETERS =[]
        params = pd.read_excel(file_path, sheet_name="bloc type", engine="openpyxl", header=5)
        params = params[params.columns[1]]
        params = enumerate(params)
        for i, param in params:
            self.PARAMETERS.append({
                "name": param,
                "ligne": i + 1,
                "colonne": 2
            })
            
        self._file_path = file_path

    def get_param_value(self, param_name) -> object:
        param = list(filter(lambda x:x["name"] == param_name, self.PARAMETERS))
        if len(param) <=0:
            return {
                "name":"Parameter Unidentify",
                "ligne":0,
                "colonne":0
            }
        return param[0]

    def steps(self, limit:int) -> list:
        params = pd.read_excel(self._file_path, sheet_name="parametre", engine="openpyxl", header=None)
        s, step = 0, int(params.iat[0,2])
        steps = []
        while s<limit:
            steps.append(s)
            s = step + s
            
        return steps