import pandas as pd
from rrm import readmission_risk_model

def main(data_file,output_file):
    
    file = open(output_file,"a")
    
    all_data = pd.read_csv(data_file)
    
    krumholz_data = readmission_risk_model(all_data, True)
    
    
    file.write("Patient ID "+ "," + "Risk "+","+"Percentage\n")
    for i,j in krumholz_data.items():
        
        file.write(i+','+str(j[1])+'\n')
        print(f"Patient ID:- {i} , Risk :- {j[1]}")


main("./HF_Model_Data.csv","Risk_Analysis.csv")