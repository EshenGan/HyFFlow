import pandas as pd
import tkinter as tk
import CI_window as Colwellwindow

#make a dataframe which mean the rainfall of all station
def colwellforall(dframe):
    dframe[dframe.columns[0]] = pd.to_datetime(dframe[dframe.columns[0]])
    dframe['mean'] = dframe.mean(axis=1)
    data = dframe[[dframe.columns[0], 'mean']].copy()
    return data


def colwellsplit(dframe, colnum):
    data = dframe[[dframe.columns[0], dframe.columns[colnum]]].copy()  # df should be the original excel file
    data[data.columns[0]] = pd.to_datetime(data[data.columns[0]])  # set 1st col as datetime,assume 1st col always date
    return data
    

# code for stations option UI
def selectwinfunction(df, mainroot,rd):
    selectwindow = tk.Toplevel(mainroot)
    selectwindow.iconbitmap('iconlogo.ico')
    df2 = df.iloc[:, 1:].copy()
    length = len(df2.columns)
    var = tk.IntVar()
    var.set(0)
    tk.Label(selectwindow, text="""Choose a rainfall station""", justify=tk.LEFT, padx=20).pack()
    #create radio button for mean
    tk.Radiobutton(selectwindow, text='all stations', indicatoron=0, width=22, padx=20, variable=var, value=0).pack(anchor=tk.W)
    # create radio button for each station
    for i in range(length):
        a = i + 1
        tk.Radiobutton(selectwindow, text=df2.columns[i], indicatoron=0, width=22, padx=20, variable=var, value=a).pack(anchor=tk.W)

    def _continue():
        g = var.get()

        if g == 0:

            resultdf = colwellforall(df)

        else:
            resultdf = colwellsplit(df, g)
        # pass the choice and dataframe to ci_window to do calculation
        selectwindow.withdraw()
        Colwellwindow.ci_window(resultdf, selectwindow,rd)
        

    def quit_me():
        selectwindow.quit()
        selectwindow.destroy()

    tk.Button(selectwindow, text='OK', command=_continue).pack(anchor=tk.W)
    selectwindow.protocol("WM_DELETE_WINDOW", quit_me)
    selectwindow.mainloop()
