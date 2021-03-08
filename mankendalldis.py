import tkinter as tk
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_pdf import PdfPages
from tkinter import filedialog
import kendall as ke


def displaymankendall(root,result,isExporting):
    root.withdraw()
    displayroot=tk.Toplevel(root)
    figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=displayroot)
    plot_widget = canvas.get_tk_widget()


    df1=pd.DataFrame(result, columns = ['result'])
    lst = [[df1.result[0], df1.result[1], df1.result[2], df1.result[3], df1.result[4],df1.result[5],df1.result[6],df1.result[7],df1.result[8]]]
    df=DataFrame(lst,columns=['trend', 'h', 'p', 'z', 'Tau', 's', 'var_s', 'slope', 'intercept'])



    def _quit():
        plt.clf()
        displayroot.destroy()

    tk.Button(displayroot, text='Quit', command=_quit).grid(row=2, column=1)

    plot_widget.grid(row=0, column=0)

    def Save():

        plt.savefig('ManKendall.pdf')

    tk.Button(displayroot, text='Save', command=Save).grid(row=2, column=0)
    plot_widget.grid(row=0, column=0)

    plt.clf()
    df1=df.copy()
    ke.kendallshow(df1)

    if isExporting:
        plt.savefig('Man Kendall.pdf')
        displayroot.destroy()
    def quit_me():
        displayroot.quit()


    displayroot.protocol("WM_DELETE_WINDOW", quit_me)
    displayroot.mainloop()




   


