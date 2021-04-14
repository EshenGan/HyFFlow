import pymannkendall as mk
import pandas as pd
import tkinter as tk
import calendar
from tkinter import Button, StringVar
import mkdisplay as mnd

def monthrange(df, startmonth, endmonth):
    dframe=df.copy()
    dframe['month'] = pd.DatetimeIndex(dframe.index).month
    dframe['counter'] = range(len(dframe))
    dframe['Date']=dframe.index
    dframe.set_index('counter',inplace=True)

    if startmonth > endmonth:

        for i in range(len(dframe)):
            if dframe.loc[i, 'month']>endmonth and dframe.loc[i, 'month']< startmonth:
                dframe.drop(index=i,inplace=True)
    elif startmonth == endmonth:
        for i in range(len(dframe)):
            if dframe.loc[i, 'month']!=startmonth:
                dframe.drop(index=i,inplace=True)
    else:
        for i in range(len(dframe)):
            if dframe.loc[i, 'month'] > endmonth or dframe.loc[i, 'month']<startmonth:
                dframe.drop(index=i, inplace=True)

    data=dframe[['Date',dframe.columns[0]]].copy()
    data.set_index(data['Date'],inplace=True)
    data.drop(columns = ['Date'], inplace = True)
    return data

def selectmonthfunc(selectroot,df):
    selectroot.withdraw()
    selectroot.iconbitmap('iconlogo.ico')
    monthwindow = tk.Toplevel(selectroot)
    OPTIONS = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    ] 

    variable = StringVar(monthwindow)
    variable.set(OPTIONS[0]) # default value
    variable2 = StringVar(monthwindow)
    variable2.set(OPTIONS[0]) # default value
    tk.Label(monthwindow, text="""Select start month""",justify=tk.LEFT, padx=20).pack()
    tk.OptionMenu(monthwindow, variable, *OPTIONS).pack(anchor=tk.W)
    tk.Label(monthwindow, text="""Select end month""",justify=tk.LEFT, padx=20).pack()
    tk.OptionMenu(monthwindow, variable2, *OPTIONS).pack(anchor=tk.W)
  
    def ok():
        start_month_abbr=variable.get()
        int_start=list(calendar.month_abbr).index(start_month_abbr)
        end_month_abbr=variable2.get()
        int_end=list(calendar.month_abbr).index(end_month_abbr)
        #call split month function and run it
        selectedmonths=monthrange(df,int_start,int_end)
        result=mk.original_test(selectedmonths)
        #call new window
        mnd.displaymankendall(monthwindow,result)

    Button(monthwindow, text="OK", command=ok).pack(anchor=tk.W)

    def quit_me():
        monthwindow.quit()

        selectroot.deiconify()

    monthwindow.protocol("WM_DELETE_WINDOW", quit_me)
    monthwindow.mainloop()