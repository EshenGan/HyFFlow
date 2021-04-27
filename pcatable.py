import tkinter as tk
import save as savee
import matplotlib.pyplot as plt
import pca_ahcdendo as pp
import dendogram as dd
import matplotlib
matplotlib.use('TkAgg')


def displaypca(root, result):
    root.withdraw()
    tableroot = tk.Toplevel(root)
    tableroot.iconbitmap('iconlogo.ico')
    df1 = result.copy()

    def _quit():
        plt.clf()
        tableroot.destroy()

    tk.Button(tableroot, text='Quit', command=_quit).grid(row=2, column=1)

    def save():
        savee.savepng1('PCA')

    tk.Button(tableroot, text='Save', command=save).grid(row=2, column=0)

    def dendo():
        dd.displaydendo(tableroot, df1)

    tk.Button(tableroot, text='dendrogram', command=dendo).grid(row=2, column=0)
    pp.pcaplot(tableroot, df1)

    def quit_me():
        tableroot.quit()
        tableroot.destroy()
        root.quit()
        root.destroy()

    tableroot.protocol("WM_DELETE_WINDOW", quit_me)
    tableroot.mainloop()
