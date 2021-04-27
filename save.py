import os
import time
import statsmodels.api as sm
import matplotlib
import matplotlib.pyplot as plt
from tkinter import messagebox
matplotlib.use('TkAgg')


def savepng1(filename):
    fullfilename = filename + time.strftime(" %Y-%m-%d %H%M%S") + ".png"  # filename string with timestamp
    path = os.path.abspath('SavedFiles')  # path to folder named SavedFiles
    # check if there is such folder exist
    # if doesnt, create a new one with specific folder name
    if not os.path.exists(path):
        os.mkdir(path)
        plt.savefig(os.path.join(path, fullfilename))
    # if exist, use it
    else:
        plt.savefig(os.path.join(path, fullfilename))  # save plots as images with filename specified above in path specified above
    messagebox.showinfo("Information", "Successfully saved in SavedFiles folder")

def savepng2(filename, figure):
    fullfilename = filename + time.strftime(" %Y-%m-%d %H%M%S") + ".png"
    path = os.path.abspath('SavedFiles')
    if not os.path.exists(path):
        os.mkdir(path)
        figure.savefig(os.path.join(path, fullfilename))
    else:
        figure.savefig(os.path.join(path, fullfilename))  # save plots as images with filename specified above in path specified above
    messagebox.showinfo("Information", "Successfully saved in SavedFiles folder")

def saveexcel(filename, model):
    aov_table = sm.stats.anova_lm(model)
    fullfilename = filename + time.strftime(" %Y-%m-%d %H%M%S")+".xlsx"
    path = os.path.abspath('SavedFiles')
    if not os.path.exists(path):
        os.mkdir(path)
        aov_table.to_excel(os.path.join(path, fullfilename))
    else:
        aov_table.to_excel(os.path.join(path, fullfilename))  # save plots as images with filename specified above in path specified above
    messagebox.showinfo("Information", "Successfully saved in SavedFiles folder")