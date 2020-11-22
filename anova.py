import tkinter as tk
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import statsmodels.api as sm

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


from pandas import DataFrame

def anovaa(df, root):
    dataf = pd.melt(df.reset_index(), value_vars = df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace = True)
    dataf['rainfall'].replace('', np.nan, inplace = True)
    dataf.dropna(subset = ['rainfall'], inplace = True)
    
    import anovafunctions as an
    
    new_window(root)
    plt.clf()

    # anova analysis 
    model = ols('rainfall ~ C(rainfallstations)', data = dataf).fit()
    aov_table = sm.stats.anova_lm(model)

    an.anova_table(aov_table)

def posthoc(df, root):
    dataf = pd.melt(df.reset_index(), value_vars = df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace = True)
    dataf['rainfall'].replace('', np.nan, inplace = True)
    dataf.dropna(subset = ['rainfall'], inplace = True)

    import anovafunctions as an

    new_window(root)
    plt.clf()
    an.anova_posthoc(dataf)

def barchart(df, root):
    df.drop(["Date"], axis = 1, inplace = False)
    dataf = pd.melt(df.reset_index(), value_vars = df.columns.values)
    dataf.columns = ['rainfallstations', 'rainfall']
    indexname = dataf[dataf['rainfallstations'] == 'Date'].index
    dataf.drop(indexname, inplace = True)
    dataf['rainfall'].replace('', np.nan, inplace = True)
    dataf.dropna(subset = ['rainfall'], inplace = True)

    import anovafunctions as an
    
    new_window(root)
    plt.clf()
    an.barchart(dataf)

def new_window(root):
    figure, ax1 = plt.subplots(figsize = (13,5), dpi = 100)
    Top=tk.Toplevel(root)
    canvas = FigureCanvasTkAgg(figure, master=Top)
    plot_widget = canvas.get_tk_widget()
    def _quit():
        plt.clf() 
        Top.destroy()
    tk.Button(Top, text = 'Quit', command = _quit).grid(row=2, column=0)
        
    plot_widget.grid(row=0, column=0)
