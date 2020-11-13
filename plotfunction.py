import pandas as pd
import numpy as np


import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
from pandas import DataFrame

from cal_return import calculate_return2
from cal_return import split_years


root = tk.Tk()

fig, ax = plt.subplots(figsize=(15,6))
t = np.arange(0.0,3.0,0.01)
s = np.sin(np.pi*t)
plt.plot(t,s)

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()


def flowplot(data):
    data[data.columns[0]]=pd.to_datetime(data[data.columns[0]])   
    data['months'] = data[data.columns[0]].apply(lambda x:x.strftime('%B'))
    data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year
    data_annualmax=data.groupby(data['year']).max()

    df3=split_years(data)
    col=data[data.columns[1]]
    maxi=col.max()
    mini=col.min()

    data_dischargesorted=calculate_return2(data,data.columns[1])
    n=len(df3)
    for y in range(n-1):
        datalist= DataFrame(df3[y],columns=data.columns)
        dataplot=calculate_return2(datalist,datalist.columns[1])
        dataplotdes=dataplot.sort_values(by= dataplot.columns[2],ascending=False)
        colum=dataplotdes[dataplotdes.columns[2]]
        col=dataplot[dataplot.columns[2]]
        culmax=col.max()
        culmin=col.min()
        if culmax==maxi or culmin==mini:
            temp=dataplot.groupby('year',as_index=False).count()
            temp.set_index('year')
            c=temp.year[0]
            plt.plot(dataplot['exceeding probability'],colum,label=c)
        else:
            plt.plot(dataplot['exceeding probability'],colum)
            
        
        plt.legend()



      
        plt.xlabel('exceeding probability')
        plt.ylabel('Discharge')
        plt.xlim(0,100)
        plt.title("Annual Flow duration")

def hydrograph(df):
    fig = plt.figure(figsize=(15,6))
    gs = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
    ax = plt.subplot(gs[1])
    
    df[df.columns[0]]=pd.to_datetime(df[df.columns[0]])
    df['months'] = df[df.columns[0]].apply(lambda x:x.strftime('%B'))
    df['year'] = pd.DatetimeIndex(df[df.columns[0]]).year

    try1=ax.plot(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean(),'g-', label='median')#plot monthly mean
    try2=ax.plot(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean().rolling(12).mean(),'r', label='moving average')#plot moving average 

    ax.set_ylabel(df.columns[1], color='b')
    ax.set_xlabel(df.columns[0])

    ax.set_xlim(df[df.columns[0]].min(), df[df.columns[0]].max())
    ax.set_ylim(0, df[df.columns[1]].max()*1.2)

    ax2 = plt.subplot(gs[0])
    df2=DataFrame(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean()).reset_index()


    try3=ax2.bar(df2[df2.columns[0]],df2[df2.columns[1]],width=10, label='median rainfall')

    ax2.xaxis.grid(b=True, which='major', color='.7', linestyle='-')
    ax2.yaxis.grid(b=True, which='major', color='0.7', linestyle='-')
    ax2.set_xlim(df2[df2.columns[0]].min(), df[df.columns[0]].max())
    ax2.yaxis.set_label_position("right")
    ax2.yaxis.tick_right()
    ax2.set_xticks([])
    ax.legend()

    ax2.set_ylabel(df2.columns[1], color='b')
    plt.tight_layout()
    ax2.invert_yaxis()
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.show()

def floodcurve(data):
    data[data.columns[0]]=pd.to_datetime(data[data.columns[0]])
    #dg = data.groupby(pd.Grouper(key='Time', freq='1W')).sum()#way to group by week
    data['months'] = data[data.columns[0]].apply(lambda x:x.strftime('%B'))#add new row month with month name January etc
    data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year
    data_annualmax=data.groupby(data['year']).max()
    data_annualmax['year']=data_annualmax.index

    df2=calculate_return(data_annualmax,data_annualmax.columns[1])
    plt.scatter(df2['Tp'],df2[df2.columns[2]],label="Tp estimated",color="blue")
    plt.plot(df2['Tp t'],df2[df2.columns[2]],label="Tp theoritical",color="orange")
        
        
    plt.xlim(1,100)
    plt.xscale("log")
        
    plt.xlabel('return period')
    plt.ylabel('Peak streamflow (cfs)')
    plt.title(" Flood frequency curve")
    plt.legend()


def medianmonthDis(data):
    data[data.columns[0]]=pd.to_datetime(data[data.columns[0]])
    #dg = data.groupby(pd.Grouper(key='Time', freq='1W')).sum()#way to group by week
    data['months'] = data[data.columns[0]].apply(lambda x:x.strftime('%B'))#add new row month with month name January etc
    data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year

    data_monthmedian=DataFrame(data.groupby(data['months']).median()).reset_index()


    plt.bar(data_monthmedian.months,data_monthmedian[data_monthmedian.columns[1]])
    plt.xlabel('months')
    plt.ylabel('Discharge (m/s)')
    plt.title("Median of Month")

    
def medianmonthRain(data):
    data[data.columns[0]]=pd.to_datetime(data[data.columns[0]])
    #dg = data.groupby(pd.Grouper(key='Time', freq='1W')).sum()#way to group by week
    data['months'] = data[data.columns[0]].apply(lambda x:x.strftime('%B'))#add new row month with month name January etc
    data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year

    data_monthmedian=DataFrame(data.groupby(data['months']).median()).reset_index()


    plt.bar(data_monthmedian.months,data_monthmedian[data_monthmedian.columns[2]])
    plt.xlabel('months')
    plt.ylabel('Rainfall (m/s)')
    plt.title("Median of Month")
