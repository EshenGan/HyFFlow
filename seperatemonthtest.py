import numpy as np
import pymannkendall as mk
import pandas as pd




# df1=pd.read_excel(r'C:\Users\kumab\Desktop\main\monthlyrainfall.xlsx')
# df=mn.mannkendalltest(df1,1)
# startmonth=1
# endmonth=1
def seperatemonthtest(df,startmonth,endmonth):
    dframe=df.copy()
    dframe['month'] = pd.DatetimeIndex(dframe.index).month
    dframe['counter'] = range(len(dframe))
    dframe['Date']=dframe.index
    dframe.set_index('counter',inplace=True)

    if startmonth > endmonth:

        for i in range(len(dframe)):
            if dframe.loc[i, 'month']>endmonth and dframe.loc[i, 'month']< startmonth:
                dframe.drop(index=i,inplace=True)
    elif startmonth==endmonth:
        for i in range(len(dframe)):
            if dframe.loc[i, 'month']!=startmonth:
                dframe.drop(index=i,inplace=True)
    else:
        for i in range(len(dframe)):
            if dframe.loc[i, 'month']>endmonth or dframe.loc[i, 'month']<startmonth:
                dframe.drop(index=i,inplace=True)

    data=dframe[['Date',dframe.columns[0]]].copy()
    data.set_index(data['Date'],inplace=True)
    data.drop(columns = ['Date'], inplace = True)
    return data
