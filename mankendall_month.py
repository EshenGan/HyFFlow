import numpy as np
import pymannkendall as mk
import pandas as pd
import tkinter as tk
import calendar
from tkinter import Button, StringVar
from tkinter.ttk import OptionMenu
import seperatemonthtest as smt
import mankendalldis as mnd

def selectmonthfunc(selectroot,df):
    selectroot.withdraw()
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
        smt_df=smt.seperatemonthtest(df,int_start,int_end)
        result=mk.original_test(smt_df)
        #call new window
        mnd.displaymankendall(monthwindow,result,0)



    
    button = Button(monthwindow, text="OK", command=ok).pack(anchor=tk.W)

    def quit_me():
        monthwindow.quit()

        selectroot.deiconify()

    monthwindow.protocol("WM_DELETE_WINDOW", quit_me)
    monthwindow.mainloop()