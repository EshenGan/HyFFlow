import tkinter as tk
import save as savee
from matplotlib import gridspec
import plots4p1 as pf
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt



def flood_curve(root,data):
    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        Top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            savee.savepng1('Flood Frequency Curve')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    new_window(root)
    plt.clf() # clear plot first
    pf.floodcurve(data)

def flow_curve(root,data):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        Top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            savee.savepng1('Flow Duration Curve')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    df=data.copy()
    new_window(root)
    plt.clf() # clear plot first
    pf.flowplot(df)
    

def hydroOnly(root, data):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        Top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            savee.savepng1('Hydrograph')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    df = data.copy()
    new_window(root)
    plt.clf()  # clear plot first
    pf.hydrographOnly(df)
    

def hydro_graph(root, data, data2):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        Top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()


        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            savee.savepng1('Hydrograph and Hyetograph')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)

    df = data.copy()
    df2 = data2.copy()
    new_window(root)
    plt.clf()  # clear plot first
    g = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
    pf.hydrograph(df, df2, g)



    


def medianDischarge(root, data):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        Top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def save():
            savee.savepng1('Median Discharge')

        tk.Button(Top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    df=data.copy()
    new_window(root)
    plt.clf()  # clear plot first
    pf.medianmonthDis(df)

def median_Rain(root, data2):

    def new_window(root):
        fig, ax = plt.subplots(figsize=(12, 6))
        Top = tk.Toplevel(root)
        Top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig, master=Top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def Save():
            savee.savepng1('Median Rainfall')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
    
    df = data2.copy()
    l = len(data2.columns)-1
    Top2 = tk.Toplevel(root)
    var = tk.IntVar()
    var.set(0)

    tk.Radiobutton(Top2, text='all columns', variable=var, value=0).pack(anchor=tk.W)
    for i in range(l):
        b = i+1
        tk.Radiobutton(Top2, text=data2.columns[i+1], variable=var, value=b).pack(anchor=tk.W)

    def _continue():
        g=var.get()
        Top2.destroy()
        
        plt.clf() # clear plot first
        new_window(root)

        pf.medianmonthRain(df, g)
    tk.Button(Top2, text='OK', command=_continue).pack(anchor=tk.W)
    

    








