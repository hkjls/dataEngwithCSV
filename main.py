from modules.extractData import extractor
from modules.AnalyseData import Analyser
import pandas as pd
from modules.refresh_file import df_from_excel
from modules.modifiyContent import ModifyContent

def main():
    "Data Extraction from CSV file"
    extract = extractor()
    extract.data = 6 # Extraction à partir du 6è lignes
    data = extract.data
    
    print(data)
    
    # process = ModifyContent()
    # process.clearContent('Collage saturne', rows_range=23062)
    
    # "Data Analysis"
    # analysis = Analyser()
    # analysis.copySheets()
    # analysis.copyContent(data, "Collage saturne")
    # file_path = analysis.saveAnalyser()
    
    # "Output Configuration"
    # df_result = df_from_excel(file_path, sheet_name="calcul (2)")
    # # df_result = pd.read_excel(file_path, sheet_name="calcul (2)")
    # machine_debit = df_result[['machine', 'Débit entrée saturne', 'Débit opérationnel']]

    # mti_pf_solystic_tae_08 = machine_debit[machine_debit['machine'] == 'MTI PF SOLYSTIC TAE 08']
    # mti_pf_solystic_tae_09 = machine_debit[machine_debit['machine'] == 'MTI PF SOLYSTIC TAE 09']
    # mti_pf_solystic_tae_10 = machine_debit[machine_debit['machine'] == 'MTI PF SOLYSTIC TAE 10']       
    
    # print(machine_debit['machine'])
if __name__ == "__main__":
    main()