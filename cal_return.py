import pandas as pd
import numpy as np



def calculate_return(df, colname):
    '''
    Add Documentation Here


    '''
    # Sort data smallest to largest
    sorted_data = df.sort_values(colname)
    
    # Count total obervations
    n = sorted_data.shape[0]
    
    # Add a numbered column 1 -> n to use in return calculation for rank
    sorted_data.insert(0, 'rank', range(1, 1 + n))
    
    # Calculate probability
    sorted_data["probability"] = (n - sorted_data["rank"] + 1) / (n + 1)
    
    # Calculate return - data are daily to then divide by 365?
    sorted_data["return-years"] = (1 / sorted_data["probability"])

    return(sorted_data)



def calculate_return2(df, colname):
    '''
    Add Documentation Here


    '''
    # Sort data smallest to largest
    sorted_data = df.sort_values(colname)
    
    # Count total obervations
    n = sorted_data.shape[0]
    
    # Add a numbered column 1 -> n to use in return calculation for rank
    sorted_data.insert(0, 'rank', range(1, 1 + n))
    
    # Calculate probability
    sorted_data["frequency"] = n /sorted_data["rank"]
    
    # Calculate return - data are daily to then divide by 365?
    sorted_data["exceeding probability"]=(1/sorted_data["frequency"])*100

    return(sorted_data)