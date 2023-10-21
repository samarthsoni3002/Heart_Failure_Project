import pandas as pd
from rrm import readmission_risk_model

def main(data_file,output_file):
    all_data = pd.read_csv(data_file)
    
    krumholz_data = readmission_risk_model(all_data, True)
    
    for i,j in krumholz_data.items():
        
        print(f"Patient ID:- {i} , Risk :- {j[1]}")


main("./HF_Model_Data.csv")