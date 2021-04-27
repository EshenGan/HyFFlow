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
    #melting rainfaill stations columns
    dataf = pd.melt(df.reset_index(), value_vars=df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']

    #dropping date column as it is not used
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace=True)

    #dropping NA values to have accurate anova results
    dataf['rainfall'].replace('', np.nan, inplace=True)
    dataf.dropna(subset=['rainfall'], inplace=True)

    #creating window for table result
    def new_window(root1):
        figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(figure, master=top)
        plot_widget = canvas.get_tk_widget()

        #quit button
        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)

        plot_widget.grid(row=0, column=0)

        #save button
        def save():
            savee.saveexcel('ANOVA', model)

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top

    new_window(root)
    plt.clf()
    # anova analysis from statsmodels
    model = ols('rainfall ~ C(rainfallstations)', data=dataf).fit()
    aov_table = sm.stats.anova_lm(model)
    an.anova_table(aov_table)


def posthoc(df, root):
    #melting rainfaill stations columns
    dataf = pd.melt(df.reset_index(), value_vars=df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']

    #dropping date column as it is not used
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace=True)

    #dropping NA values to have accurate anova post hoc results
    dataf['rainfall'].replace('', np.nan, inplace=True)
    dataf.dropna(subset=['rainfall'], inplace=True)

    #creating window for table results
    def new_window(root1):
        figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(figure, master=top)
        plot_widget = canvas.get_tk_widget()

        #quit button
        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)

        plot_widget.grid(row=0, column=0)

        #save button
        def save():
            savee.savepng1('ANOVA_Post_Hoc')

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top

    new_window(root)
    plt.clf()
    an.anova_posthoc(dataf)


def barchart(df, root):
    #melting rainfaill stations columns
    dataf = pd.melt(df.reset_index(), value_vars=df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']

    #dropping date column as it is not used
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace=True)

    #dropping na values
    dataf['rainfall'].replace('', np.nan, inplace=True)
    dataf.dropna(subset=['rainfall'], inplace=True)

    #creating window for the bar chart
    def new_window(root1):
        figure, ax1 = plt.subplots(figsize=(13, 7), dpi=100)
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(figure, master=top)
        plot_widget = canvas.get_tk_widget()

        #quit button
        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)

        plot_widget.grid(row=0, column=0)

        #save button
        def save():
            savee.savepng1('Rainfall stations Mean Chart')

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top

    new_window(root)
    plt.clf()
    an.barchart(dataf)
