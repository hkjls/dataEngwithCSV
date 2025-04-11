from tkinter import filedialog
from pathlib import Path

class configureFile:
    
    def __init__(self, file_path):
        self.ROOT = f"{Path().resolve()}/Data"
        self.file_path = file_path
        self._max_columns: int = self.max_columns()
    
    def max_columns(self) -> int:    
        columns_lengths = []
        with open(self.file_path, "r", encoding="utf-8") as file:
            for row in file:
                columns = row.strip().split(";")
                columns_lengths.append(len(columns))
        
        max_column = max(columns_lengths)
        return max_column
        
    def file(self):
        output_file: str = f"{self.ROOT}/{self.file_path.split("/")[-1]}"
        
        with open(self.file_path, "r", encoding="utf-8") as sf, open(output_file, "w", encoding="utf-8") as of:
            for row in sf:
                parts = row.strip().split(";")
                while len(parts) < self._max_columns:
                    parts.append("")
                
                row_padded = ";".join(parts)
                of.write(row_padded + "\n")
                
if __name__ == "__main__":
    source_file = filedialog.askopenfilename(
        title="Which file you want to transform",
        filetypes=(("CSV file", "*.csv"), ("All file", "*.*"))
    )
    csv_file = configureFile(source_file)
    csv_file.file()
    