import tkinter as tk
from matplotlib import gridspec

import plotfunction as pf
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
from tkinter import ttk, filedialog, messagebox

def new_window(root):
    fig ,ax= plt.subplots(figsize=(12,6))
    Top=tk.Toplevel(root)
    canvas = FigureCanvasTkAgg(fig, master=Top)
    plot_widget = canvas.get_tk_widget()
    def _quit():
        plt.clf() 
        Top.destroy()
    tk.Button(Top, text = 'Quit', command = _quit).grid(row=2, column=0)   
    plot_widget.grid(row=0, column=0)


def flood_curve(root,data):
    if data!=None:
        new_window(root)
        plt.clf() # clear plot first
        pf.floodcurve(data)
    else:
        messagebox.showerror("Information", "The data is empty")
def flow_curve(root,data):
    if data!=None:
        df=data.copy()
        new_window(root)
        plt.clf() # clear plot first
        pf.flowplot(df)
    else:
        messagebox.showerror("Information", "The data is empty")

def hydroOnly(root,data):
    if data!=None:
        df=data.copy()
        new_window(root)
        plt.clf() # clear plot first
        pf.hydrographOnly(df)
    else:
        messagebox.showerror("Information", "The data is empty")

def hydro_graph(root,data,data2):
    if data!=None and data2!=None:
        df=data.copy()
        df2=data2.copy()
        new_window(root)
        plt.clf() # clear plot first
        g = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
        pf.hydrograph(df,df2,g)
    else:
        messagebox.showerror("Information", "The data is empty")


def medianDischarge(root,data):
    if data!=None:
        df=data.copy()
        new_window(root)
        plt.clf() # clear plot first
        pf.medianmonthDis(df)
    else:
        messagebox.showerror("Information", "The data is empty")



def median_Rain(root,data2):
    if data2!=None:
        df=data2.copy()
        l=len(data2.columns)-1
        Top2=tk.Toplevel(root)
        var = tk.IntVar()
        var.set(0)

        tk.Radiobutton(Top2,text='all columns',variable=var, value=0).pack(anchor=tk.W)
        for i in range(l):
            b=i+1
            tk.Radiobutton(Top2,text=data2.columns[i+1],variable=var, value=b).pack(anchor=tk.W)
    else:
        messagebox.showerror("Information", "The data is empty")
    
    def _continue():
        g=var.get()
        Top2.destroy()
        
        plt.clf() # clear plot first
        new_window(root)

        pf.medianmonthRain(df,g)    
    tk.Button(Top2, text = 'OK', command = _continue).pack(anchor=tk.W)
    

    







