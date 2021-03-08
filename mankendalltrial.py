import numpy as np
import pandas as pd
import pymannkendall as mk
import matplotlib.pyplot as plt
import statsmodels.api as sm
def RemoveNA(df):
    df[df.columns[1]].replace('', np.nan, inplace = True)
    df.dropna(inplace = True)


df=pd.read_excel(r"C:\Users\kumab\Desktop\main\Telok Buing Discharge.xlsx",index_col='Date/Time' )


result=mk.original_test(df,alpha=0.05)

print(result)





            


