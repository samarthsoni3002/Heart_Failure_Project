# Readmission Risk Model:- https://www.ncbi.nlm.nih.gov/pubmed/10618565
# Risk is calculated as mentioned by H M Krumholz and other authors in this paper.


def readmission_risk_model(data, exclude_under_65):
    
    score_data = {}
    
    for patient in range(len(data)):
        
        
        if exclude_under_65 and int(data["Age"][patient]) > 65:
            continue
        
        count = 0
        
        if float(data["Creatinine"][patient]) > 2.5: count += 1
        if int(data["Prior_12_hosp"][patient]) == 1: count += 1
        
        if int(data["Prior_HF"][patient]) == 1: count += 1
        if int(data["Diabetes"][patient]) == 1: count += 1
        
        risk = "Low, 26%"
        
        if count == 1 or count == 2: risk = "Medium, 48%"
        
        if count == 3 or count == 4: risk = "High, 59%"
        
        score_data[str(data["PAT_ID_D"][patient])] = (count,risk)
        
    return score_data
     
     
     
     
     
 
