import tkinter as tk
import save as savee
import pandas as pd
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
matplotlib.use('TkAgg')


def tableplot(df):
    ax = plt.subplot()
    ax.axis('off')
    ax.set_title('Man-Kendall Test')
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1.2, 2.5)


def displaymankendall(root, result):
    root.withdraw()
    displayroot = tk.Toplevel(root)
    displayroot.iconbitmap('iconlogo.ico')
    figure, ax = plt.subplots(figsize=(13, 5))
    canvas = FigureCanvasTkAgg(figure, master=displayroot)
    plot_widget = canvas.get_tk_widget()
    df = pd.DataFrame(result, columns=['result'])
    listt = [[df.result[0], df.result[1], df.result[2], df.result[3], df.result[4], df.result[5], df.result[6], df.result[7], df.result[8]]]
    df1 = DataFrame(listt, columns=['trend', 'h', 'p', 'z', 'Tau', 's', 'var_s', 'slope', 'intercept'])

    plt.clf()
    df = df1.copy()
    tableplot(df)

    def _quit():
        plt.clf()
        displayroot.destroy()

    tk.Button(displayroot, text='Quit', command=_quit).grid(row=2, column=1)

    plot_widget.grid(row=0, column=0)

    def save():
        savee.savepng1('Man-Kendall Classic Test')

    tk.Button(displayroot, text='Save', command=save).grid(row=2, column=0)
    plot_widget.grid(row=0, column=0)

    def quit_me():
        displayroot.quit()
        displayroot.destroy()

    displayroot.protocol("WM_DELETE_WINDOW", quit_me)
    displayroot.mainloop()
