import tkinter as tk
import os
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pca_ahcdendo as pp
matplotlib.use('TkAgg')


def displaydendo(root, result):
    root.withdraw()
    dendoroot = tk.Toplevel(root)
    dendoroot.iconbitmap('iconlogo.ico')
    figure, ax1 = plt.subplots(figsize=(13, 5), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=dendoroot)
    plot_widget = canvas.get_tk_widget()

    def _quit():
        plt.clf()
        dendoroot.destroy()

    tk.Button(dendoroot, text='Quit', command=_quit).grid(row=2, column=1)
    plot_widget.grid(row=0, column=0)

    def save():
        path = os.path.abspath('SavedFiles')
        file = 'AHC Dendogram.png'
        plt.savefig(os.path.join(path, file))

    tk.Button(dendoroot, text='Save', command=save).grid(row=2, column=0)

    plt.clf()
    df1 = result.copy()
    pp.dendoplot(df1)

    def quit_me():
        dendoroot.quit()
        dendoroot.destroy()
        root.deconify()
        root.destroy()

    dendoroot.protocol("WM_DELETE_WINDOW", quit_me)
    dendoroot.mainloop()
