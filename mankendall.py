import numpy as np
import pymannkendall as mk
import pandas as pd
import tkinter as tk
import mankendall_month as man_m

def mannkendalltestforall(dframe):
    dframe[dframe.columns[0]] = pd.to_datetime(dframe[dframe.columns[0]])
    dframe.set_index(dframe.columns[0], inplace=True)
    dframe['mean'] = dframe.mean(axis=1)
    return dframe['mean']

def mannkendalltest(dframe,colnum):
    data = dframe[[dframe.columns[0],dframe.columns[colnum]]].copy()  #df should be the original excel file
    data[data.columns[0]] = pd.to_datetime(data[data.columns[0]]) # setting first col as datetime,assuming first col always the Date
    data.set_index(data.columns[0],inplace=True) # setting datetime as index
    return data
    

# code for stations option UI
def selectwinfunction(mainroot,df):
    selectwindow = tk.Toplevel(mainroot)
    df2 = df.iloc[:,1:].copy()
    l = len(df2.columns)
    var = tk.IntVar()
    var.set(0)
    tk.Label(selectwindow, text="""Choose a rainfall station""",justify=tk.LEFT, padx=20).pack()
    tk.Radiobutton(selectwindow, text='all stations',indicatoron=0,width=22, padx=20,variable=var, value=0).pack(anchor=tk.W)
    for i in range(l):
        a = i + 1
        tk.Radiobutton(selectwindow, text=df2.columns[i],indicatoron=0,width=22, padx=20,variable=var, value=a).pack(anchor=tk.W)

    def _continue():
        g = var.get()

        if g == 0:
            #function call for mann kendall test on mean rainfall from all stations#
            resultdf=mannkendalltestforall(df)
            #call select month

        else:
            resultdf=mannkendalltest(df, g)
            
        man_m.selectmonthfunc(selectwindow,resultdf)
        selectwindow.destroy()

    def quit_me():
        selectwindow.quit()
        selectwindow.destroy()

    selectwindow.protocol("WM_DELETE_WINDOW", quit_me)




    tk.Button(selectwindow, text='OK', command=_continue).pack(anchor=tk.W)
    selectwindow.mainloop()

    
