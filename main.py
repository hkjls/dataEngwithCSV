from modules.extractData import extractor
import pandas as pd
from modules.handleContent import handleContent
from utils.parameters import *
from utils.strtohour import strtotime

def main():
    "Data Extraction from CSV file"
    handle = handleContent()
    extract = extractor()
    
    #Extract Data fro
    extract.from_csv = 5 # Extraction à partir du 6è ligne
    csv = extract.from_csv
    
    param = get_param_value("DUREE DEPILAGE")
    dep_t = csv[csv.columns[param["colonne"]]].at[param["ligne"]-1]
    
    param = get_param_value("NOMBRE OBJETS DEPILES")
    inj_n = csv[csv.columns[param["colonne"]]].at[param["ligne"]-1]
    
    dep_t = strtotime(dep_t)
    db_entry = round(int(inj_n)/(dep_t*24))
    
    #Delete old data in Excel file and insert new data
    # filename = handle.set_filename("*.xlsx")
    # handle.Delete(filename=filename, sheetName="Collage saturne")
    # handle.Insert(dt=csv, targetfile=filename, sheet_name="Collage saturne")
    
    #Extract Data evaluated from Excel
    # # extract.from_excel = "calcul (2)"
    # excel = extract.from_excel
    
    # print(excel)
    
    # extract.from_excel_pd = "Collage saturne"
    # dt = extract.from_excel_pd
    
    # print(dt)
if __name__ == "__main__":
    main()