from modules.extractData import extractor
import pandas as pd
from modules.handleContent import handleContent

def main():
    "Data Extraction from CSV file"
    handle = handleContent()
    extract = extractor()
    
    #Extract Data from CSV
    # extract.from_csv = 6 # Extraction à partir du 6è lignes
    # csv = extract.from_csv
    
    #Delete old data in Excel file and insert new data
    # filename = handle.set_filename("*.xlsx")
    # handle.Delete(filename=filename, sheetName="Collage saturne")
    # handle.Insert(dt=csv, targetfile=filename, sheet_name="Collage saturne")
    
    #Extract Data evaluated from Excel
    extract.from_excel = "calcul (2)"
    excel = extract.from_excel
    
    print(excel)
    
    extract.from_excel_pd = "Collage saturne"
    dt = extract.from_excel_pd
    
    print(dt)
if __name__ == "__main__":
    main()