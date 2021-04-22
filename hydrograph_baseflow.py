import tkinter as tk
import pandas as pd
import numpy as np
import save as savee
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from pandas import DataFrame
from matplotlib.figure import Figure
from tkinter import *
from tkcalendar import *
from pandas.plotting import register_matplotlib_converters
from tkinter import messagebox
register_matplotlib_converters()
matplotlib.use('TkAgg')


def baseflowdiagram(data, root):
    fig = Figure(figsize=(12, 6))
    ax = fig.add_subplot()

    def new_window(root1):
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig, master=top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def save():
            savee.savepng2('Baseflow Diagram', fig)

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top

    df = data.copy()
    new_window(root)
    plt.cla()  # clear axis
    plt.clf()  # clear figure
    # figure s5
    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])  # change  to pandas datetime format
    df.set_index(df.columns[0], inplace=True)  # set datetime column as index
    df[df.columns[0]] = df.iloc[:, 0].astype('float64')  # convert to data type float64
    # plot bar chart of discharge against datetime
    ax.bar(df.index.values, df.iloc[:, 0], 1.85, label="discharge", snap=False)
    ax.set(xlabel="Date/Time", ylabel="Discharge(m3/s)", title="Baseflow Diagram")  # labeling and title
    ax.set_xlim(min(df.index.values), max(df.index.values))  # setting x axis limit for bar chart
    # ax.set_ylim(0,max(df['Discharge (m3/s)']))
    ax.spines['top'].set_visible(False)  # removing top black line of barchart plot place
    ax.spines['right'].set_visible(False)  # removing right black line of barchart plot place
    plt.setp(ax.get_xticklabels(), rotation=45)  # rotate x axis label direction
    plt.tight_layout()
    dfd = df.iloc[:, 0]
    # calculating baseflow(local minima) with interval of 5
    var = dfd[argrelextrema(dfd.to_numpy(dtype='float64', na_value=np.nan), np.less, order=5)[0]]
    var.interpolate()  # interpolate the data
    ax.plot(var.index.values, var, color='red', label="baseflow")  # plot baseflow line graph on top of barchart
    ax.legend()


def hydrograph_baseflow(data, root):
    def run_plot():  # function to be called to plot hydrograph with baseflow line only when date range is selected
        fig = Figure(figsize=(12, 6))
        ax = fig.add_subplot()

        def new_window(root1):
            top = tk.Toplevel(root1)
            top.iconbitmap('iconlogo.ico')
            canvas = FigureCanvasTkAgg(fig, master=top)
            plot_widget = canvas.get_tk_widget()

            def _quit():
                plt.clf()
                top.destroy()

            tk.Button(top, text='Quit', command=_quit).grid(row=2, column=1)
            plot_widget.grid(row=0, column=0)

            def save():
                savee.savepng2('Hydrograph with Baseflow', fig)

            tk.Button(top, text='Save', command=save).grid(row=2, column=0)
            plot_widget.grid(row=0, column=0)
            return top

        df = data.copy()
        new_window(root)
        plt.cla()
        plt.clf()
        # figure s6
        df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
        df.set_index(df.columns[0], inplace=True)
        # slicing discharge data according to selected date time range
        dframe = df.loc[date1.get_date().strftime("%m/%d/%Y"):date2.get_date().strftime("%m/%d/%Y")]
        # plotting hydrograph
        ax.plot(dframe.index.values, dframe.iloc[:, 0], color='blue', linestyle='-', label='discharge')
        ax.set(xlabel="Date/Time", ylabel="Discharge(m3/s)", title="Hydrograph with Baseflow")
        ax.set_xlim(min(dframe.index.values), max(dframe.index.values))
        # ax.set_ylim(0,max(df['Discharge (m3/s)']))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.setp(ax.get_xticklabels(), rotation=45)
        plt.tight_layout()
        df4 = dframe.iloc[:, 0]
        var1 = df4[argrelextrema(df4.to_numpy(na_value=np.nan, dtype='float64'), np.less, order=5)[0]]
        ax.plot(var1.index.values, var1, color='red', label='baseflow')
        ax.legend()

    datepickui = tk.Tk()
    datepickui.title("Pick range of dates")
    datepickui.geometry("200x200")
    datepickui.iconbitmap('iconlogo.ico')
    label1 = Label(datepickui, text="Starting From")
    label1.pack()
    date1 = DateEntry(datepickui, locale='en_UK', date_pattern='dd/mm/yyyy')  # editable dropdown calendar
    date1.pack()
    label2 = Label(datepickui, text="Ends at")
    label2.pack()
    date2 = DateEntry(datepickui, locale='en_UK', date_pattern='dd/mm/yyyy')
    date2.pack()

    def _continue():
        if date1 == date2:  # starting date and ending date should not be the same
            messagebox.showerror('Error!', 'Must pick a range of date')
        else:
            run_plot()
        datepickui.destroy()

    tk.Button(datepickui, text="Get Date", command=_continue).pack(pady=20)
    datepickui.mainloop()


def linear_regression(data, data2, root):
    fig = Figure(figsize=(12, 6))
    ax = fig.add_subplot()
    fig1 = Figure(figsize=(12, 6))
    ax1 = fig1.add_subplot()

    def new_window(root1):
        top = tk.Toplevel(root1)
        top.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig, master=top)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            top.destroy()

        tk.Button(top, text='Quit', command=_quit).grid(row=2, column=2)
        plot_widget.grid(row=0, column=0)

        tk.Button(top, text='Details', command=details).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def save():
            savee.savepng2('Rainfall-runoff Relations', fig)

        tk.Button(top, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top

    def details():
        new_window_2(root)
        plt.clf()
        ax1.axis('off')
        showdetails()

    def new_window_2(root2):
        top2 = tk.Toplevel(root2)
        top2.iconbitmap('iconlogo.ico')
        canvas = FigureCanvasTkAgg(fig1, master=top2)
        plot_widget = canvas.get_tk_widget()

        def _quit():
            plt.clf()
            top2.destroy()

        tk.Button(top2, text='Quit', command=_quit).grid(row=2, column=1)
        plot_widget.grid(row=0, column=0)

        def save():
            savee.savepng2('Rainfall-runoff relations Details', fig1)

        tk.Button(top2, text='Save', command=save).grid(row=2, column=0)
        plot_widget.grid(row=0, column=0)
        return top2

    df = data.copy()
    df2 = data2.copy()
    new_window(root)
    plt.clf()  # clear plot first

    # read and group discharge by month
    # df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
    dataf = DataFrame(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean())

    # compute the mean for each month the rainfall values of all  stations , put the mean in another col
    df2[df2.columns[0]] = pd.to_datetime(df2[df2.columns[0]])
    df2.set_index(df2.columns[0], inplace=True)
    rowcount = len(dataf.index)
    # df2['mean'] = df2.iloc[:, :7].mean(axis=1)  # mean column is col 7
    df2['mean'] = df2.iloc[:, :len(df2.columns)].mean(axis=1)  # mean column is col 7

    # fill up NaN
    imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
    df2['mean'] = imputer.fit_transform(df2['mean'].values.reshape(-1, 1))[:, 0]
    dataf[dataf.columns[0]] = imputer.fit_transform(dataf.iloc[:, 0].values.reshape(-1, 1))[:, 0]

    # linearly regress discharge col with mean col   lx = mean ly = discharge
    lx = df2.iloc[:rowcount, len(df2.columns)-1].values.reshape(-1, 1)
    ly = dataf.iloc[:, 0].values.reshape(-1, 1)
    lr = LinearRegression()
    lr.fit(lx, ly)

    # predict discharge using mean of rainfall
    yl = lr.predict(lx)

    # model evaluation
    rmse = mean_squared_error(ly, yl)  # root mean squared error
    r2 = r2_score(ly, yl)

    # visualize
    ax.scatter(lx, ly, label='x/y')
    ax.set(xlabel="Rainfall", ylabel="Discharge", title="Linear Regression of Discharge against Rainfall")
    ax.plot(lx, yl, color='red', label="best fit line")
    ax.legend()

    def showdetails():  # tabling of linear regression coefficient,intercept, rmse and r2
        a = np.array(lr.coef_)
        c = a.flatten()  # flatten it from 2d array to 1d
        e = np.array(lr.intercept_)
        listt = [[float(c), float(e), rmse, r2]]  # put all values into a 2d array, 1 row 4 columns
        # converting list into dataframe
        listdf = DataFrame(listt, columns=['Slope', 'Intercept', 'Root Mean Squared Error', 'R2 Score'], dtype=float)
        # insert into matplotlib table
        table = ax1.table(cellText=listdf.values, colLabels=listdf.columns, loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1.2, 2.5)
