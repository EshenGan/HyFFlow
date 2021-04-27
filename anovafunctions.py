import pandas as pd
import statsmodels.stats.multicomp as mc
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np


def anova_table(aov):
    ax = plt.subplot()
    ax.axis('off')
    ax.set_title('Anova')

    # calculate f crit
    aov['f_crit'] = scipy.stats.f.ppf(q=1-.05, dfn=aov['df'][0], dfd=aov['df'][-1])

    # total sum square and total degree of freedom
    total_ss = aov['sum_sq'][0] + aov['sum_sq'][-1]
    total_df = aov['df'][0] + aov['df'][-1]

    #creating a list to store the values
    lst = [['Between Groups', aov['sum_sq'][0], aov['df'][0], aov['mean_sq'][0], aov['F'][0], aov['PR(>F)'][0],
            aov['f_crit'][0]], ['Within Groups', aov['sum_sq'][-1], aov['df'][-1], aov['mean_sq'][-1]],
           ['Total', total_ss, total_df]]

    # storing list into dataframe
    df1 = pd.DataFrame(lst, columns=['', 'SS', 'df', 'MS', 'F', 'P-value', 'F crit'], dtype=float)

    # creating table
    table = ax.table(cellText=df1.values, colLabels=df1.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.2, 2.5)


def anova_posthoc(dataf):
    ax = plt.subplot()
    ax.axis('off')
    ax.set_title('Posthoc')

    # Tukey test / anova post hoc
    comp = mc.MultiComparison(dataf['rainfall'], dataf['rainfallstations'])
    post_hoc_res = comp.tukeyhsd()
    x = post_hoc_res.summary()

    # storing values into dataframe
    df = pd.DataFrame(x)

    # creating table
    table = ax.table(cellText=df.values, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1)


def barchart(dataf):
    ax1 = plt.subplot()
    ax1.set_title('Mean Bar Chart')

    # plotting bar chart
    df1 = dataf.groupby(dataf.columns[0]).mean()
    colors = [plt.cm.Paired(np.arange(len(df1)))]
    df1.plot(kind='bar', ax=ax1,  legend=False, color=colors)
    ax1.set_title("Rainfall Stations Mean Bar Chart")
    ax1.set_ylabel("Mean")
    ax1.set_xlabel("Rainfall Stations")
    plt.setp(ax1.get_xticklabels(), rotation=45)
