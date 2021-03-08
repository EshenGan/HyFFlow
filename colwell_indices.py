import tkinter as tk
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_pdf import PdfPages
from tkinter import filedialog
import rpy2test as ci


def colwell_indices(df, root, isExporting):
    
    def new_window(root):
        figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
        Top = tk.Toplevel(root)
        canvas = FigureCanvasTkAgg(figure, master=Top)
        plot_widget = canvas.get_tk_widget()

        if isExporting:
            Top.withdraw()

        def _quit():
            plt.clf()
            Top.destroy()

        tk.Button(Top, text='Quit', command=_quit).grid(row=2, column=1)

        plot_widget.grid(row=0, column=0)

        def Save():

            plt.savefig('Colwell Indices.pdf')

        tk.Button(Top, text='Save', command=Save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return Top

    Top = new_window(root)
    plt.clf()
    ci.cw_indices(df)

    if isExporting:
        plt.savefig('Colwell Indices.pdf')
        Top.destroy()