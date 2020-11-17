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


from pandas.plotting import register_matplotlib_converters
from pandas import DataFrame

import plotfunction as pf

def _pandas_converters():
    converters_active = check_if_active()  # something like pd.Timestamp in matplotlib.units.registry
    pd.plotting.deregister_matplotlib_converters()
    yield
    if converters_active:
        pd.plotting.register_matplotlib_converters()


root = tk.Tk()
root.geometry("500x200")

fig ,ax= plt.subplots(figsize=(15,6))

t = np.arange(0.0,3.0,0.01)
s = np.sin(np.pi*t)
plt.plot(t,s)

data = pd.read_excel('Telok Buing Discharge.xlsx')



def flood_curve():
    new_window()
    plt.clf() # clear plot first
    pf.floodcurve(data)

def flow_curve():
    new_window()
    plt.clf() # clear plot first
    pf.flowplot(data)

def hydroOnly():
    new_window()
    plt.clf() # clear plot first
    pf.hydrographOnly(data)

def hydro_graph():
    new_window()
    plt.clf() # clear plot first
    g = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
    pf.hydrograph(data,g)


def medianDischarge():
    new_window()
    plt.clf() # clear plot first
    pf.medianmonthDis(data)


def update():
    fig.canvas.draw() 

def save():
    ts = datetime.datetime.now() 
    
    date_time = ts.strftime("%m/%d/%Y, %H:%M:%S")
    plt.savefig(date_time)
  # correction: to clean the window when exit
def realquit():
    root.quit()
    root.destroy()
def new_window():
    Top=tk.Toplevel(root)
    canvas = FigureCanvasTkAgg(fig, master=Top)
    plot_widget = canvas.get_tk_widget()
    def _quit():
        plt.clf() 
        Top.destroy()
    tk.Button(Top,text="Update",command=update).grid(row=1, column=0)
    tk.Button(Top, text = 'Quit', command = _quit).grid(row=2, column=0)
    tk.Button(Top, text = 'Save', command = save).grid(row=2, column=1)
    plot_widget.grid(row=0, column=0)


tk.Button(root,text='Flood curve',command=flood_curve).grid(row=2,column=1)
tk.Button(root,text='flow curve',command=flow_curve).grid(row=3,column=1)
tk.Button(root,text='Hydrograph Only',command=hydroOnly).grid(row=4,column=1)
tk.Button(root,text='Hydrograph',command=hydro_graph).grid(row=5,column=1)
tk.Button(root,text='Median Discharge',command=medianDischarge).grid(row=6,column=1)
tk.Button(root,text='Quit',command=realquit).grid(row=2,column=0)

root.mainloop()