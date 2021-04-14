import tkinter as tk
import pandas as pd
import numpy as np
import save as savee
import anovafunctions as an
from statsmodels.formula.api import ols
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')


def anovaa(df, root):
    dataf = pd.melt(df.reset_index(), value_vars=df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace=True)
    dataf['rainfall'].replace('', np.nan, inplace=True)
    dataf.dropna(subset=['rainfall'], inplace=True)

    def new_window(root1):
        figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(figure, master=top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)

        plot_widget.grid(row=0, column=0)

        def save():
            savee.saveexcel('ANOVA', model)

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top

    new_window(root)
    plt.clf()
    # anova analysis
    model = ols('rainfall ~ C(rainfallstations)', data=dataf).fit()
    aov_table = sm.stats.anova_lm(model)
    an.anova_table(aov_table)


def posthoc(df, root):
    dataf = pd.melt(df.reset_index(), value_vars=df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace=True)
    dataf['rainfall'].replace('', np.nan, inplace=True)
    dataf.dropna(subset=['rainfall'], inplace=True)

    def new_window(root1):
        figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(figure, master=top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)

        plot_widget.grid(row=0, column=0)

        def save():
            savee.savepng1('ANOVA_Post_Hoc')

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top

    new_window(root)
    plt.clf()
    an.anova_posthoc(dataf)


def barchart(df, root):
    df.drop(["Date"], axis=1, inplace=False)
    dataf = pd.melt(df.reset_index(), value_vars=df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace=True)
    dataf['rainfall'].replace('', np.nan, inplace=True)
    dataf.dropna(subset=['rainfall'], inplace=True)

    def new_window(root1):
        figure, ax1 = plt.subplots(figsize=(13, 7), dpi=100)
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(figure, master=top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)

        plot_widget.grid(row=0, column=0)

        def save():
            savee.savepng1('Rainfall stations Mean Chart')

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top

    new_window(root)
    plt.clf()
    an.barchart(dataf)
