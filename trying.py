import tkinter as tk
import pandas as pd
import numpy as np
from matplotlib import gridspec
from tkinter.filedialog import askopenfile
import datetime

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


from pandas import DataFrame


root = tk.Tk()
root.geometry("500x200")
fig ,ax= plt.subplots(figsize=(12,6))



data = pd.read_excel('Telok Buing Discharge.xlsx')
data2=pd.read_excel('monthlyrainfall.xlsx')






def flood_curve():
    import plotfunction as pf
    new_window()
    plt.clf() # clear plot first
    pf.floodcurve(data)

def flow_curve():
    import plotfunction as pf
    new_window()
    plt.clf() # clear plot first
    pf.flowplot(data)

def hydroOnly():
    import plotfunction as pf
    new_window()
    plt.clf() # clear plot first
    pf.hydrographOnly(data)

def hydro_graph():
    import plotfunction as pf
    new_window()
    plt.clf() # clear plot first
    g = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
    pf.hydrograph(data,data2,g)


def medianDischarge():
    import plotfunction as pf
    new_window()
    plt.clf() # clear plot first
    pf.medianmonthDis(data)


def update():
    fig.canvas.draw() 


def realquit():
    root.quit()
    root.destroy()


def window_selection():
    data2=pd.read_excel('monthlyrainfall.xlsx')
    l=len(data2.columns)-1
    Top2=tk.Toplevel(root)
    var = tk.IntVar()
    var.set(0)

    tk.Radiobutton(Top2,text='all columns',variable=var, value=0).pack(anchor=tk.W)
    for i in range(l):
        b=i+1
        tk.Radiobutton(Top2,text=data2.columns[i+1],variable=var, value=b).pack(anchor=tk.W)
    
    def _continue():
        g=var.get()
        Top2.destroy()
        import plotfunction as pf
        plt.clf() # clear plot first
        new_window()

        pf.medianmonthRain(data2,g)    
    tk.Button(Top2, text = 'OK', command = _continue).pack(anchor=tk.W)
    

    




def new_window():
    Top=tk.Toplevel(root)
    canvas = FigureCanvasTkAgg(fig, master=Top)
    plot_widget = canvas.get_tk_widget()
    def _quit():
        plt.clf() 
        Top.destroy()
    tk.Button(Top,text="Update",command=update).grid(row=1, column=0)
    tk.Button(Top, text = 'Quit', command = _quit).grid(row=2, column=0)
    
    plot_widget.grid(row=0, column=0)


tk.Button(root,text='Flood curve',command=flood_curve).grid(row=2,column=1)
tk.Button(root,text='flow curve',command=flow_curve).grid(row=3,column=1)
tk.Button(root,text='Hydrograph Only',command=hydroOnly).grid(row=4,column=1)
tk.Button(root,text='Hydrograph',command=hydro_graph).grid(row=5,column=1)
tk.Button(root,text='Median Discharge',command=medianDischarge).grid(row=6,column=1)
tk.Button(root,text='Median RainFall',command=window_selection).grid(row=7,column=1)
tk.Button(root,text='Quit',command=realquit).grid(row=2,column=0)



root.mainloop()