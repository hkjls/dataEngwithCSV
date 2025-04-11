from modules.extractData import extractor
import pandas as pd
# from modules.handleContent import handleContent
from utils.strtotime import setTime
from utils.parameters import params

def main():
    "Data Extraction from CSV file"
    '''
        PREPARATION DES MODULES NECESSAIRE
        EXTRACTION : Pour extraire les deux fichiers CSV et Excel
        EVAULATION ET CONFIGURATION DES DATES/HEURES : Pour interagir les types times string et date
        RECHERCHE DES PARAMETRES : Obtenir toutes les paramètres nécessaire au calcul
    '''
    extract = extractor()
    ctime = setTime()
    param_obj = params(extract.excel_file_path)

    # Extraction à partir du 6è ligne puis affectation des données obtenu dans la variable csv
    extract.from_csv = 5
    csv = extract.from_csv
    exit()
    # print(csv)
    # print(csv.index[-1])
    
    # Création des pas obtenu à partir de la feuille de calcul paramètre
    steps_list = param_obj.steps(csv.index[-1])
    
    #DEBIT ENTREE SATURNE
    '''    Il suffit de passer le nom du paramettre dans param_obj.get_param_value() et on obtient
            un objet sous cette forme :
            {
                "name":"Parameter Unidentify",
                "ligne":0,
                "colonne":0
            }
            
            Puis pour avoir la liste de toutes les paramètres pour chaque ligne ( Excel calc (2)) il
            suffit de boucler avec le steps dans la ligne 24 de même pour les autres paramètres
    '''
    param = param_obj.get_param_value("DUREE DEPILAGE") #*
    dep_tlist = list(map(
        lambda x:ctime.strtoday(csv[csv.columns[param["colonne"]]].at[param["ligne"]+x-1]), 
        steps_list
    )) #*
    
    param = param_obj.get_param_value("NOMBRE OBJETS DEPILES") #*
    inj_nlist = list(map(
        lambda x:csv[csv.columns[param["colonne"]]].at[param["ligne"]+x-1],
        steps_list
    ))
    
    '''
        La formule pour obtenir la debit d'entrée
    '''
    db_entry_list = map(lambda x,y:int(y)/(x*24), dep_tlist, inj_nlist)
    
    #DUREE OPERATIONNELLE
    do = []
    for step in steps_list:
        param = param_obj.get_param_value("DUREE DEPILAGE") #*
        dep_t = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1] #*
    
        param = param_obj.get_param_value("DUREE ARRET CONVOYEUR EN DEFAUT") #*
        cny_dft = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1] #*
        cny_dft = ctime.strtimetosecond(cny_dft) # Convertir cny_dft de type string en type time
        
        param = param_obj.get_param_value("DUREE ARRET LIGNE AC")
        line_ac = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
        line_ac = ctime.strtimetosecond(line_ac)/2  # Convertir cny_dft de type string en type time

        param = param_obj.get_param_value("DUREE ARRET LIGNE BD")
        line_bd = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
        line_bd = ctime.strtimetosecond(line_bd)/2  # Convertir cny_dft de type string en type time
        
        param = param_obj.get_param_value("DUREE BOURRAGE DEPILEUR")
        brg_dpl = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
        brg_dpl = ctime.strtimetosecond(brg_dpl)  # Convertir cny_dft de type string en type time
        
        t = cny_dft + line_ac + line_bd + brg_dpl
        dep_t = ctime.strtimetosecond(dep_t)
        
        '''
            La formule pour obtenir la duree operationnelle
        '''
        do.append(ctime.timetostr((dep_t + t)/3600))
        
    #NBR D'OBJETS EN TRI DEFINITIF + SOUS-PROG
    tri_def_list = []
    for step in steps_list:
        param = param_obj.get_param_value("TRI DEFINITIF")
        tri_definitif = csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1]
        param = param_obj.get_param_value("A RETRIER (sous-programme)")
        '''
            La formule pour obtenir les nombres d'objets en tri definitif 
        '''
        tri_definitif = int(tri_definitif) + int(csv[csv.columns[param["colonne"]]].at[param["ligne"]+step-1])
        tri_def_list.append(tri_definitif)
        
    do_time = list(map(lambda x:ctime.strtoday(x), do)) #Conversion de toutes les duree operationnel de type string en type time
    db_op:list = []
    SESSION = ctime.strtoday(str(param_obj.SESSION)) #la variable SESSION dans la feuille parametre
    
    '''
        Ici on ne recupère que les dureé operationnel supperieur a SESSION qui est 00:06:00
    '''
    for i, d in enumerate(do_time):
        db_op_el = 0
        if d > SESSION:
            db_op_el = tri_def_list[i]/(d*24)
            
        db_op.append(db_op_el)
    
    #MACHINE
    param = param_obj.get_param_value("MACHINE")
    machines = list(map(lambda x:csv[csv.columns[param["colonne"]]].at[param["ligne"]+x-1], steps_list))
    
    #ETIQUETTES DE LIGNES
    param = param_obj.get_param_value("DATE DEBUT SESSION")
    date = list(map(lambda x:csv[csv.columns[param["colonne"]]].at[param["ligne"]+x-1], steps_list))
    
    info_machines = []
    i = 0
    
    '''
        CONFIGURATION DE DATAFRAME DE SORTIE
        
    '''
    for mch, d, db_el,dt in zip(machines, db_op, db_entry_list, date):
        #Mettre les données dans un liste de objet avec les clès name, date, entry debit et operational Debit
        info_machines.append({
                "name":mch,
                "date":dt,
                "Entry Debit":db_el,
                "Operational Debit":d
            })
        
    machine_list = list(set(machines)) #Supperssion des doublons
    
    for mch in sorted(machine_list):
        #Sortir les infos de chaque matèrial par nom et ayant les Débits opérationnels supperieur à 0
        info_per_machine = list(filter(lambda x:x["name"] == mch and x["Operational Debit"] > 0, info_machines))
        df_machines = {}
        for i, info in enumerate(info_per_machine):
            df_machines[f"{i}"] = info
        
        df = pd.DataFrame.from_dict(df_machines, orient="index")
        
        print(df)
    
if __name__ == "__main__":
    #Lancement des l'application :)
    main()