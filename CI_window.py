import tkinter as tk
import save as savee
import matplotlib
import matplotlib.pyplot as plt
import Colwell as Cw
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')


def ci_window(df, root,rd):
    
    def new_window(root1):
        #set canvas
        figure, ax = plt.subplots(figsize=(13, 5), dpi=100)
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(figure, master=top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def save():
            savee.savepng1('Colwell Indices')

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top
    # call function to plot
    window = new_window(root)
    plt.clf()
    df2=df.copy()
    Cw.cw_indices(df2)
    
    def quit_me():

        window.destroy()
        if rd ==1:
            root.quit()
            root.destroy()

    window.protocol("WM_DELETE_WINDOW", quit_me)
