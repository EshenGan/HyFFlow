import pandas as pd
import numpy as np
import datetime as dt
import math

def calculate_return(df, colname):
    '''
    Add Documentation Here


    '''
    # Sort data smallest to largest
    sorted_data = df.sort_values(colname,ascending=False)
    
    # Count total obervations
    n = sorted_data.shape[0]
    
    # Add a numbered column 1 -> n to use in return calculation for rank
    sorted_data.insert(0, 'rank', range(1, 1 + n))
    sorted_data = sorted_data.sort_values(colname,ascending=True)
    # Calculate probability
    sorted_data["q1"] = (sorted_data['rank']-0.44) / (n + 1 - 2 * 0.44)
    sorted_data["p1"]=1-sorted_data["q1"]
    sorted_data["Tp"]=1/(1-sorted_data["p1"])


    s=sorted_data[colname].std()
    a=math.sqrt(6)*s/math.pi
    u=sorted_data[colname].mean()-0.5772*a
    print(a)
    sorted_data["x-u/a"]=(sorted_data[colname]-u)/a
    sorted_data["p theoritical"]=np.exp(-np.exp(-sorted_data["x-u/a"]))
    sorted_data["Tp t"]=1/(1-sorted_data["p theoritical"])
    # Calculate return - data are daily to then divide by 365?

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

def split_years(df):
    df['year'] = df['Date/Time'].dt.year
    return [df[df['year'] == y] for y in df['year'].unique()]