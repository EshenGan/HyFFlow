import pandas as pd
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pandas import DataFrame

def flowplot(df):
    #plot flow of duration
    data=df.copy()
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
        if culmax==maxi:
            temp=dataplot.groupby('year',as_index=False).count()
            temp.set_index('year')
            c=temp.year[0]
            tr=plt.plot(dataplot['exceeding probability'],colum,label=c)
        elif culmin==mini:
            temp=dataplot.groupby('year',as_index=False).count()
            temp.set_index('year')
            c=temp.year[0]
            try2=plt.plot(dataplot['exceeding probability'],colum,label=c)
        else:
            plt.plot(dataplot['exceeding probability'],colum,label=None)
            
    plt.legend()    
    plt.xlabel('exceeding probability')
    plt.ylabel('Discharge')
    plt.xlim(0,100)
    plt.title("Annual Flow duration")
    return data_dischargesorted

def hydrograph(df,data,gs):
    #plot hydro with hyeto
    ax = plt.subplot(gs[1])
    df[df.columns[0]]=pd.to_datetime(df[df.columns[0]])   
    df['months'] = df[df.columns[0]].apply(lambda x:x.strftime('%B'))
    df['year'] = pd.DatetimeIndex(df[df.columns[0]]).year

    dfmean=DataFrame(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean()).reset_index()
    try1=ax.plot(dfmean[dfmean.columns[0]],dfmean[dfmean.columns[1]],'b-', label='mean')#plot monthly mean
    try2=ax.plot(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean().rolling(10).mean(),'r', label='moving average')#plot moving average 

    ax.set_ylabel(df.columns[1], color='b')
    ax.set_xlabel(dfmean.columns[0])
    
    ax.set_xlim(df[df.columns[0]].min(), df[df.columns[0]].max())
    ax.set_ylim(0, dfmean[dfmean.columns[1]].max()*1.2)

    ax2 = plt.subplot(gs[0])
    data['mean'] = data.mean(axis=1)

    try3=ax2.bar(data[data.columns[0]],data['mean'], label='mean rainfall',color='black',width=5,snap=False)

    ax2.xaxis.grid(b=True, which='major', color='.7', linestyle='-')
    ax2.yaxis.grid(b=True, which='major', color='0.7', linestyle='-')
    ax2.set_xlim(df[df.columns[0]].min(), df[df.columns[0]].max())
    ax2.set_ylim(data['mean'].min(), data['mean'].max())

    ax2.yaxis.set_label_position("right")

    ax2.yaxis.tick_right()
    ax2.set_xticks([])
    ax.legend()
    ax2.set_ylabel('RainFall', color='b')
    plt.tight_layout()
    ax2.invert_yaxis()
    plt.gcf().subplots_adjust(bottom=0.15)

def hydrographOnly(df):
    #plot hydro 
    
    df[df.columns[0]]=pd.to_datetime(df[df.columns[0]])
    df['months'] = df[df.columns[0]].apply(lambda x:x.strftime('%B'))
    df['year'] = pd.DatetimeIndex(df[df.columns[0]]).year
    dfmean=DataFrame(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean()).reset_index()
    print(dfmean)
    try1=plt.plot(dfmean[dfmean.columns[0]],dfmean[dfmean.columns[1]],'b-', label='median')#plot monthly mean
    try2=plt.plot(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean().rolling(10).mean(),'r', label='moving average')#plot moving average 

    plt.ylabel(df.columns[1], color='b')
    plt.xlabel(df.columns[0])
    plt.xlim(df[df.columns[0]].min(), df[df.columns[0]].max())
    plt.ylim(0, dfmean[dfmean.columns[1]].max()*1.2)

    plt.legend()
    plt.tight_layout()
    plt.gcf().subplots_adjust(bottom=0.15)

def floodcurve(df):
    data=df.copy()
    #plot flood duration curve
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
    return df2


def medianmonthDis(data):
    #median of discharge group by month
    data[data.columns[0]]=pd.to_datetime(data[data.columns[0]])
    #dg = data.groupby(pd.Grouper(key='Time', freq='1W')).sum()#way to group by week
    data['months'] = data[data.columns[0]].apply(lambda x:x.strftime('%B'))#add new row month with month name January etc
    data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year
    data['month'] = pd.DatetimeIndex(data[data.columns[0]]).month
    data=data.sort_values(by=data.columns[1])
    data_monthmedian=DataFrame(data.groupby([data['month'],data['months']])[data.columns[1]].median()).reset_index()

    plt.bar(data_monthmedian.months,data_monthmedian[data.columns[1]])
    plt.ylim(0,data_monthmedian[data_monthmedian.columns[2]].max()*1.2)
    plt.xlabel('months')
    plt.ylabel('Discharge (m/s)')
    plt.title("Median of Month")

    
def medianmonthRain(data,g):
    if g==0:
        #plot median of rainfall group by month
        data[data.columns[0]]=pd.to_datetime(data[data.columns[0]])
        data['mean'] = data.mean(axis=1)
        #dg = data.groupby(pd.Grouper(key='Time', freq='1W')).sum()#way to group by week
        data['months'] = data[data.columns[0]].apply(lambda x:x.strftime('%B'))#add new row month with month name January etc
        data['month'] = pd.DatetimeIndex(data[data.columns[0]]).month
        data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year
        #print(data.sort_values(by=['months']))
    
        #data_monthmedian=DataFrame(data.groupby(data['months'])['mean'].median()).reset_index()
        data_monthmedian=DataFrame(data.groupby([data['month'],data['months']])['mean'].median()).reset_index()
        plt.bar(data_monthmedian.months,data_monthmedian['mean'])
        plt.xlabel('months')
        plt.ylabel('Rainfall (m/s)')
        plt.title("Median of Month")
        data.drop(columns=['month', 'months','year'])
        
    else:
        data[data.columns[0]]=pd.to_datetime(data[data.columns[0]])
        data['months'] = data[data.columns[0]].apply(lambda x:x.strftime('%B'))#add new row month with month name January etc
        data['month'] = pd.DatetimeIndex(data[data.columns[0]]).month
        data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year
        data_monthmedian=DataFrame(data.groupby([data['month'],data['months']])[data.columns[g]].median()).reset_index()
        plt.bar(data_monthmedian.months,data_monthmedian[data.columns[g]])
        plt.xlabel('months')
        plt.ylabel('Rainfall (m/s)')
        plt.title("Median of Month of "+data.columns[g])
        data.drop(columns=['month', 'months','year'])
        



#function used
def calculate_return(df, colname):
    # Sort data smallest to largest
    sorted_data = df.sort_values(colname,ascending=False)
    
    # Count total obervations
    n = sorted_data.shape[0]
    
    # Add a numbered column 1 -> n to use in return calculation for rank
    sorted_data.insert(0, 'rank', range(1, 1 + n))
    sorted_data = sorted_data.sort_values(colname,ascending=True)
    # Calculate probability
    sorted_data["q1"] = (sorted_data['rank']-0.44) / (n + 1 - 2 * 0.44)
    sorted_data["p1"]=1-sorted_data["q1"]
    sorted_data["Tp"]=1/(1-sorted_data["p1"])


    s=sorted_data[colname].std()
    a=math.sqrt(6)*s/math.pi
    u=sorted_data[colname].mean()-0.5772*a

    sorted_data["x-u/a"]=(sorted_data[colname]-u)/a
    sorted_data["p theoritical"]=np.exp(-np.exp(-sorted_data["x-u/a"]))
    sorted_data["Tp t"]=1/(1-sorted_data["p theoritical"])
    # Calculate return - data are daily to then divide by 365?

    return(sorted_data)



def calculate_return2(df, colname):
    # Sort data smallest to largest
    sorted_data = df.sort_values(colname)
    
    # Count total obervations
    n = sorted_data.shape[0]
    
    # Add a numbered column 1 -> n to use in return calculation for rank
    sorted_data.insert(0, 'rank', range(1, 1 + n))
    
    # Calculate probability
    sorted_data["frequency"] = n /sorted_data["rank"]
    
    # Calculate return - data are daily to then divide by 365?
    sorted_data["exceeding probability"]=(1/sorted_data["frequency"])*100

    return(sorted_data)

def split_years(df):
    df['year'] = df['Date/Time'].dt.year
    return [df[df['year'] == y] for y in df['year'].unique()]

