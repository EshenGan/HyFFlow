import tkinter as tk
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_pdf import PdfPages
from tkinter import filedialog
import pcaplot as pp
import dendodis as dd

def displaypca(root,result,isExporting):
    root.withdraw()
    displayroot=tk.Toplevel(root)
    figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=displayroot)
    plot_widget = canvas.get_tk_widget()
    plt.clf()
    df1=result.copy()
    def _quit():
        plt.clf()
        displayroot.destroy()

    tk.Button(displayroot, text='Quit', command=_quit).grid(row=2, column=1)

    plot_widget.grid(row=0, column=0)

    def Save():

        plt.savefig('pcaplot.pdf')

    tk.Button(displayroot, text='Save', command=Save).grid(row=2, column=0)



    def dendo():
        dd.displaydendo(df1)

    tk.Button(displayroot, text='dendo', command=dendo).grid(row=2, column=0)


    
    pp.pcaplot(df1)


