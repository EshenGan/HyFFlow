import os
import time
import statsmodels.api as sm
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def savepng1(filename):
    fullfilename = filename + time.strftime(" %Y-%m-%d %H%M%S") + ".png"
    path = os.path.abspath('SavedFiles')
    plt.savefig(os.path.join(path, fullfilename))


def savepng2(filename, figure):
    fullfilename = filename + time.strftime(" %Y-%m-%d %H%M%S") + ".png"
    path = os.path.abspath('SavedFiles')
    figure.savefig(os.path.join(path, fullfilename))


def saveexcel(filename, model):
    aov_table = sm.stats.anova_lm(model)
    fullfilename = filename + time.strftime(" %Y-%m-%d %H%M%S")+".xlsx"
    path = os.path.abspath('SavedFiles')
    aov_table.to_excel(os.path.join(path, fullfilename))
