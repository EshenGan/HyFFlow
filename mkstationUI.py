import pandas as pd
import tkinter as tk
import mkmonthUI as man_m

# function to get the mean of all station
def allstationsmean(dframe):
    dframe[dframe.columns[0]] = pd.to_datetime(dframe[dframe.columns[0]])  # changing to datetime format
    dframe['mean'] = dframe.mean(axis=1)  # calcuating mean of all columns in each row and putting mean value in  'mean' column
    data=dframe[[dframe.columns[0],'mean']].copy()  # copying date and mean columns over to a new dataframe
    data.set_index(data.columns[0], inplace=True)  # setting date as index of dataframe
    return data

# function to split and choose one station
def splitstations(dframe,colnum):
    data = dframe[[dframe.columns[0],dframe.columns[colnum]]].copy()  #df should be the original excel file
    data[data.columns[0]] = pd.to_datetime(data[data.columns[0]]) # setting first col as datetime,assuming first col always the Date
    data.set_index(data.columns[0],inplace=True) # setting datetime as index
    return data
    

# function to generate stations selection UI
def choosestation(mainroot,df):
    selectwindow = tk.Toplevel(mainroot)
    selectwindow.iconbitmap('iconlogo.ico')
    df2 = df.iloc[:,1:].copy()  # copying all rows and all columns except first column over to a new dataframe
    l = len(df2.columns)  # find the number of columns
    var = tk.IntVar()
    var.set(0)  # set initial value as 0
    # buttons that represent each different rainfall station
    tk.Label(selectwindow, text="""Choose a rainfall station""",justify=tk.LEFT, padx=20).pack()
    # 0 represents all stations/mean
    tk.Radiobutton(selectwindow, text='all stations',indicatoron=0,width=22, padx=20,variable=var, value=0).pack(anchor=tk.W)
    # 1 and above each different number represents each different station
    for i in range(l):
        a = i + 1
        tk.Radiobutton(selectwindow, text=df2.columns[i],indicatoron=0,width=22, padx=20,variable=var, value=a).pack(anchor=tk.W)

    def _continue():
        g = var.get()

        if g == 0:  # if value return from button is 0 indicates 'all stations' option is chosen
            resultdf = allstationsmean(df)


        else:  # if otherwise indicates a specific station is chosen
            resultdf = splitstations(df, g)
            
        man_m.selectmonthfunc(selectwindow,resultdf)  # calls in function that generates months selection UI

    tk.Button(selectwindow, text='OK', command=_continue).pack(anchor=tk.W)  # button that invokes _continue() function 

    def quit_me():
        selectwindow.quit()
        selectwindow.destroy()

    selectwindow.protocol("WM_DELETE_WINDOW", quit_me)
    selectwindow.mainloop()
