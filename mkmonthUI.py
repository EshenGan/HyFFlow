import pymannkendall as mk
import pandas as pd
import tkinter as tk
import calendar
from tkinter import Button, StringVar
import mkdisplay as mnd

def monthrange(df, startmonth, endmonth):
    dframe=df.copy()
    # add month and counter column
    dframe['month'] = pd.DatetimeIndex(dframe.index).month
    dframe['counter'] = range(len(dframe))
    #reset the date column from index
    dframe['Date']=dframe.index
    # set back index to counter
    dframe.set_index('counter',inplace=True)
    # statement to get the interval of month between start and end
    #if start>end example start=12 end =2
    if startmonth > endmonth:
        # drop all row which >end and <start example  start=12 end =2 drop 3,4,5,6..11
        for i in range(len(dframe)):
            if dframe.loc[i, 'month']>endmonth and dframe.loc[i, 'month']< startmonth:
                dframe.drop(index=i,inplace=True)
    # if start is end drop all which is not that month
    elif startmonth == endmonth:
        for i in range(len(dframe)):
            if dframe.loc[i, 'month']!=startmonth:
                dframe.drop(index=i,inplace=True)
    # start<end
    else:
        #drop all which is not between start and end
        for i in range(len(dframe)):
            if dframe.loc[i, 'month'] > endmonth or dframe.loc[i, 'month']<startmonth:
                dframe.drop(index=i, inplace=True)

    data=dframe[['Date',dframe.columns[0]]].copy()
    data.set_index(data['Date'],inplace=True)
    data.drop(columns = ['Date'], inplace = True)
    return data
# provide option for start month and end month
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
        #convert month string to integer
        int_start=list(calendar.month_abbr).index(start_month_abbr)
        end_month_abbr=variable2.get()
        #convert month string to integer
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