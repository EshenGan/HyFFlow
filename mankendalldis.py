import tkinter as tk
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_pdf import PdfPages
from tkinter import filedialog

def displaymankendall(root,result):
    root.withdraw()
    displayroot=tk.Toplevel(root)
    figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=displayroot)
    plot_widget = canvas.get_tk_widget()

    ax1 = plt.subplot()
    ax1.axis('off')
    ax1.set_title('Man-Kendall Test')

    df1=pd.DataFrame(result, columns = ['result'])
    lst = [[df1.result[0], df1.result[1], df1.result[2], df1.result[3], df1.result[4],df1.result[5],df1.result[6],df1.result[7],df1.result[8]]]
    df=DataFrame(lst,columns=['trend', 'h', 'p', 'z', 'Tau', 's', 'var_s', 'slope', 'intercept'])

    table = ax1.table(cellText = df.values, colLabels = df.columns, loc = 'center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.2,2.5)
    def Save():

            plt.savefig('Mankendall.pdf')
    def quit_me():
        displayroot.quit()
        displayroot.destroy()
    tk.Button(displayroot, text='Save', command=Save).grid(row=2, column=0)

    tk.Button(displayroot, text='Quit', command=quit_me).grid(row=2, column=1)
    

    displayroot.protocol("WM_DELETE_WINDOW", quit_me)
    displayroot.mainloop()


   


