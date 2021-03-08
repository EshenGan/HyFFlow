import tkinter as tk
from matplotlib import gridspec

import plotfunction as pf
import matplotlib
matplotlib.use('TkAgg')
from tkinter.filedialog import asksaveasfile

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
from tkinter import ttk, filedialog, messagebox

from matplotlib.backends.backend_pdf import PdfPages




def flood_curve(root,data):
    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            plt.savefig('Flood frequency.png')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    new_window(root)
    plt.clf() # clear plot first
    pf.floodcurve(data)




    
def flow_curve(root,data):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            plt.savefig('Flow duration.png')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    df=data.copy()
    new_window(root)
    plt.clf() # clear plot first
    pf.flowplot(df)
    

def hydroOnly(root,data):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            plt.savefig('hydroOnly.png')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    df=data.copy()
    new_window(root)
    plt.clf() # clear plot first
    pf.hydrographOnly(df)
    

def hydro_graph(root,data,data2):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()


        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():

            plt.savefig('Hydrograph and hyetrograph.png')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)

    df=data.copy()
    df2=data2.copy()
    new_window(root)
    plt.clf() # clear plot first
    g = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
    pf.hydrograph(df,df2,g)



    


def medianDischarge(root,data):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            plt.savefig('Median Discharge.png')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    df=data.copy()
    new_window(root)
    plt.clf() # clear plot first
    pf.medianmonthDis(df)
    



def median_Rain(root,data2):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            plt.savefig('Median RainFall.png')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    df=data2.copy()
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
        
        plt.clf() # clear plot first
        new_window(root)

        pf.medianmonthRain(df,g)    
    tk.Button(Top2, text = 'OK', command = _continue).pack(anchor=tk.W)
    

    








