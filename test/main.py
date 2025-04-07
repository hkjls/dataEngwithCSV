from modules.extractData import extractor
import pandas as pd
from modules.handleContent import handleContent
from utils.parameters import *
from utils.strtotime import setTime
from utils.parameters import params

def main():
    "Data Extraction from CSV file"
    # handle = handleContent()
    ctime = setTime()
    extract = extractor()
    param_obj = params(extract.excel_file_path)
    #Extract Data fro
    extract.from_csv = 5 # Extraction à partir du 6è ligne
    csv = extract.from_csv
    
    steps_list = param_obj.steps(csv.index[-1])
    
    #DEBIT ENTREE SATURNE
    param = param_obj.get_param_value("DUREE DEPILAGE")
    dep_tlist = list(map(
        lambda x:ctime.strtoday(csv[csv.columns[param["colonne"]]].at[param["ligne"]+x-1]), 
        steps_list
    ))
    
    param = param_obj.get_param_value("NOMBRE OBJETS DEPILES")
    inj_nlist = list(map(
        lambda x:csv[csv.columns[param["colonne"]]].at[param["ligne"]+x-1],
        steps_list
    ))
    
    
    db_entry_list = map(lambda x,y:round(int(y)/(x*24)), dep_tlist, inj_nlist)
    
    #DUREE OPERATIONNELLE
    do = []
    for step in steps_list:
        param = param_obj.get_param_value("DUREE DEPILAGE")
        dep_t = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
    
        param = param_obj.get_param_value("DUREE ARRET CONVOYEUR EN DEFAUT")
        cny_dft = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
        cny_dft = ctime.strtimetosecond(cny_dft)
        
        param = param_obj.get_param_value("DUREE ARRET LIGNE AC")
        line_ac = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
        line_ac = ctime.strtimetosecond(line_ac)/2

        param = param_obj.get_param_value("DUREE ARRET LIGNE BD")
        line_bd = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
        line_bd = ctime.strtimetosecond(line_bd)/2
        
        param = param_obj.get_param_value("DUREE BOURRAGE DEPILEUR")
        brg_dpl = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
        brg_dpl = ctime.strtimetosecond(brg_dpl)
        
        t = cny_dft + line_ac + line_bd + brg_dpl
        # t_ind = ctime.timetostr(t/3600)
        dep_t = ctime.strtimetosecond(dep_t)
        do.append(ctime.timetostr((dep_t + t)/3600))
    
    #MACHINE
    param = param_obj.get_param_value("MACHINE")
    machines = list(map(lambda x:csv[csv.columns[param["colonne"]]].at[param["ligne"]+x-1], steps_list))
    
    info_machines = {}
    i = 0
    
    for mch, d, db_el in zip(machines, do, db_entry_list):
        info_machines[f"row{i}"]={
                "name":mch,
                "Entry Debit":db_el,
                "Operational Debit":d
            }
        i += 1
        
    df = pd.DataFrame.from_dict(info_machines, orient="index")
    print(df)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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