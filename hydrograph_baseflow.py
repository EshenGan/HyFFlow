import tkinter as tk
from tkinter import *
from tkcalendar import *
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from pandas import DataFrame
from matplotlib.figure import Figure
from Hydrograph.hydrograph import sepBaseflow

fig = Figure(figsize=(12,6))
ax= fig.add_subplot()
def new_window(root):

    
    Top=tk.Toplevel(root)
    canvas = FigureCanvasTkAgg(fig, master=Top)
    plot_widget = canvas.get_tk_widget()
    def _quit():
        plt.clf() 
        Top.destroy()
    tk.Button(Top, text = 'Quit', command = _quit).grid(row=2, column=0)   
    plot_widget.grid(row=0, column=0)
    Top.protocol("WM_DELETE_WINDOW", _quit)

def baseflowdiagram(data,root):
    df=data.copy()
    new_window(root)
    ax.cla()
    plt.clf() # clear plot first
    # figure s5
    df['Date/Time']= pd.to_datetime(df['Date/Time'])
    df.set_index('Date/Time', inplace=True)

    df['Discharge (m3/s)'] = df['Discharge (m3/s)'].astype('float64')
    ax.bar(df.index.values, df['Discharge (m3/s)'],1.85,label="discharge",snap=False)
    ax.set(xlabel ="Date/Time",ylabel = "Discharge(m3/s)",title = "Hydrograph")
    ax.set_xlim(min(df.index.values), max(df.index.values))
    # ax.set_ylim(0,max(df['Discharge (m3/s)']))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    dfd = df['Discharge (m3/s)']
    var = dfd[argrelextrema(dfd.to_numpy(dtype='float64', na_value=np.nan), np.less, order=5)[0]]
    var.interpolate()
    ax.plot(var.index.values,var, color='red',label="baseflow")
    ax.legend()



def hydrograph_baseflow(data,root):
    df=data.copy()
    new_window(root)
    ax.cla()
    plt.clf() # clear plot first
    # figure s6
    #df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
    #df.set_index(df.columns[0], inplace=True)
    df['Date/Time']=pd.to_datetime(df['Date/Time'])
    df.set_index('Date/Time', inplace=True)

    #datepicker
    #rooT= Tk()
    #rooT.title()
    #rooT.geometry("600x400")
    #def grab_date

    dframe = df.loc["1/1/1967":"2/15/1967"]
    ax.plot(dframe.index.values, dframe['Discharge (m3/s)'],color='blue', linestyle='-',label='discharge')
    ax.set(xlabel ="Date/Time",ylabel = "Discharge(m3/s)",title = "Hydrograph")
    ax.set_xlim(min(dframe.index.values), max(dframe.index.values))
    # ax.set_ylim(0,max(df['Discharge (m3/s)']))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    df4 = dframe['Discharge (m3/s)']
    var1 = df4[argrelextrema(df4.to_numpy( na_value=np.nan,dtype='float64'), np.less, order=5)[0]]
    #print(var1)
    var1.interpolate()
    print(var1)
    ax.plot(var1.index.values,var1, color='red',label='baseflow')
    ax.legend()


def linear_regression(data,data2,root):
    df=data.copy()
    df2=data2.copy()
    new_window(root)
    plt.cla()
    plt.clf() # clear plot first
    
    # read and group discharge by month
    df['Date/Time']= pd.to_datetime(df['Date/Time'])
    dataf= DataFrame(df.groupby(pd.Grouper(key='Date/Time', freq='1M'))[df.columns[1]].mean())

    # compute the mean for each month the rainfall values of all  stations , put the mean in another col
    df2['Date']= pd.to_datetime(df2['Date'])
    df2.set_index('Date', inplace=True)
    rowcount = len(dataf.index)
    df2['mean'] = df2.iloc[:, :7].mean(axis=1) # mean column is col 7

    # fill up NaN
    imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
    df2['mean'] = imputer.fit_transform(df2['mean'].values.reshape(-1, 1))[:, 0]
    dataf['Discharge (m3/s)'] = imputer.fit_transform(dataf['Discharge (m3/s)'].values.reshape(-1,1))[:,0]

    # linearly regress discharge col with mean col   lx = mean ly = discharge
    lx = df2.iloc[:rowcount, 7].values.reshape(-1, 1)
    ly = dataf.iloc[:, 0].values.reshape(-1, 1)
    lr = LinearRegression()
    lr.fit(lx, ly)

    # predict discharge using mean of rainfall
    yl = lr.predict(lx)

    #model evaluation
    rmse = mean_squared_error(ly,yl)
    r2 = r2_score(ly,yl)

    #visualize
    ax.scatter(lx, ly,label='x/y')
    ax.set(xlabel="Rainfall", ylabel="Discharge", title="Linear Regression of Discharge against Rainfal")
    ax.plot(lx, yl, color='red',label="best fit line")
    ax.legend()

    #printing values
    print('Slope: ',lr.coef_)
    print('Intercept: ',lr.intercept_)
    print('Root mean squared error:' ,rmse)
    print('R2 score: ',r2)


