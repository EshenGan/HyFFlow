import pandas as pd
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.stats.multicomp as mc
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *
import numpy as np
from prettytable import PrettyTable

dataf = pd.read_excel(r'D:\UNMC\CSAI Year 2\Software Engineering Group Project\Project Documents\rainfall.xlsx')
dataf.drop('date', axis = 1, inplace = True)

root = tk.Tk()

def anova():
    # compute overall_mean
    #overall_mean = df['rainfall'].mean()

    # compute group_mean
    #group_mean = df.groupby('rainfallstation').mean()

    # compute sum of squares between groups
    #ss_between = sum((df['overall_mean'] - df['group_mean'])**2)
    ss_between = 2267.35374

    # compute sum of squares within groups
    #ss_within = sum((df['rainfall'] - df['group_mean'])**2)
    ss_within = 67932.2752

    # compute sum of squares total
    ss_total = ss_within + ss_between
    ss_total = float("%0.3f"%ss_total)

    # compute degree of freedom between groups
    #k = len(set(df['rainfallstation']))
    k = 7
    df_between = k - 1

    # compute degree of freedom within groups
    #n = df.shape[0]
    n = 2483 
    df_within = n - k

    # compute degree of freedom total
    df_total = n - 1

    # compute mean squares between groups
    ms_between = ss_between / df_between
    ms_between = float("%0.5f"%ms_between)

    # compute mean squares within groups
    ms_within = ss_within / df_within
    ms_within = float("%0.7f"%ms_within)

    # compute F statistic
    F = ms_between / ms_within
    F = float("%0.7f"%F)

    # compute p_value
    p_value = 1 - scipy.stats.f.cdf(F, df_between, df_within)

    # compute F crit
    f_crit = scipy.stats.f.ppf(q = 1-.05, dfn = df_between, dfd = df_within)
    f_crit = float("%0.8f"%f_crit)

    aovt = PrettyTable(['', 'SS', 'df', 'MS', 'F', 'P-value', 'F crit'])
    aovt.add_row(['Between Groups', ss_between, df_between, ms_between, F, p_value, f_crit])
    aovt.add_row(['Within Groups', ss_within, df_within, ms_within, 'NA', 'NA', 'NA'])
    aovt.add_row(['Total', ss_total, df_total, 'NA', 'NA', 'NA', "NA"])
    text = Text(root, height = 8, width = 103)
    text.insert(INSERT, aovt)
    text.config(state=DISABLED)
    text.pack()

def anova_table(aov):

    model = ols('rainfall ~ C(rainfallstations)', data = dataf).fit()
    aov_table = sm.stats.anova_lm(model)

    aov['f_crit'] = scipy.stats.f.ppf(q = 1-.05, dfn = aov['df'][0], dfd = aov['df'][-1])

    cols = ['sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)', 'f_crit']
    aov = aov[cols]
    anova_table(aov_table)
    print(anova_table(aov_table))
    return aov

def anova_posthoc():

    comp = mc.MultiComparison(dataf['rainfall'], dataf['rainfallstations'])
    post_hoc_res = comp.tukeyhsd()
    post_hoc_res.summary()
    print(post_hoc_res.summary())
    text = Text(root, height = 10, width = 103)
    text.insert(INSERT, post_hoc_res.summary())
    text.config(state=DISABLED)
    text.pack()

root.title("Post Hoc Test")

def barchart():
    figure = plt.Figure(figsize = (10,10), dpi = 100)
    ax1 = figure.add_subplot(111)
    bar = FigureCanvasTkAgg(figure, root)
    bar.get_tk_widget().pack(side = tk.LEFT, fill = tk.BOTH)
    df = dataf.groupby('rainfallstations').mean()
    df.plot(kind = 'bar', legend = False, ax = ax1, color = [plt.cm.Paired(np.arange(len(df)))])
    ax1.set_title("Rainfallstations mean")
    ax1.set_ylabel("Mean")

button1 = Button(root, text = 'open', command = barchart)
button1.pack()
button2 = Button(root, text = 'opeeen', command = anova)
button2.pack()

root.mainloop()

# still doing it