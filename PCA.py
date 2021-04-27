import pandas as pd
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from sklearn.decomposition import PCA
from pandas import DataFrame
from plots4p1 import flowplot
from plots4p1 import floodcurve


def pcapreprocess(data, dryperiodstart, dryperiodend, wetperiodstart, wetperiodend):
    df = data.copy()
    dataflowplot = flowplot(df)
    datafloodplot = floodcurve(df)
    plt.clf()
    plt.close()
    df['Discharge (m3/s)'] = df['Discharge (m3/s)'].astype('float64')
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df.set_index('Date/Time', inplace=True)

    df['Discharge (m3/s)'] = df['Discharge (m3/s)'].astype('float64')
    # baseflow calculation
    dfd = df['Discharge (m3/s)']
    var = dfd[argrelextrema(dfd.to_numpy(dtype='float64', na_value=np.nan), np.less, order=5)[0]]
    var.interpolate()
    var1 = DataFrame(var)
    var1.reset_index(inplace=True)
    var1.set_index(var1['Date/Time'], inplace=True)
    var1 = var1.resample('D').sum()

    df['base'] = var1[var1.columns[0]]

    df['base'] = df['base'].fillna(0)
    df['diff'] = df[df.columns[0]] - df['base']
    # extract date which base =discharge
    data = df.loc[df['diff'] == 0].copy()
    durations = [None] * len(data)
    for i in range(len(data) - 1):
        durations[i] = data.index[i + 1] - data.index[i]

    data.reset_index(inplace=True)
    data[data.columns[0]] = pd.to_datetime(data[data.columns[0]])
    data['duration'] = None
    # caculate duration between first row date to second row date and etc
    for l in range(len(data) - 1):
        data.loc[l, ['duration']] = durations[l].days
    # set date to datetimeindes
    data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year
    data['month'] = pd.DatetimeIndex(data[data.columns[0]]).month

    data['period'] = None
    # label each days with period
    if dryperiodstart < dryperiodend:
        for i in range(len(data)):
            if data.loc[i, 'month'] >= dryperiodstart and data.loc[i, 'month'] <= dryperiodend:
                data.loc[i, 'period'] = 'dry'
    else:
        for i in range(len(data)):
            if data.loc[i, 'month'] <= dryperiodend or data.loc[i, 'month'] >= dryperiodstart:
                data.loc[i, 'period'] = 'dry'

    if wetperiodstart < wetperiodend:
        for i in range(len(data)):
            if data.loc[i, 'month'] >= wetperiodstart and data.loc[i, 'month'] <= wetperiodend:
                data.loc[i, 'period'] = 'wet'
    else:
        for i in range(len(data)):
            if data.loc[i, 'month'] <= wetperiodend or data.loc[i, 'month'] >= wetperiodstart:
                data.loc[i, 'period'] = 'wet'

    startyear = data['year'].min()
    endyear = data['year'].max()
    n_ofyear = endyear - startyear
    datalist = list()
    for i in range(n_ofyear):
        datalist.append(data.loc[data['year'] == startyear + i])

    datalist2 = list()
    for i in range(len(datalist)):
        datalist2.append(datalist[i].loc[datalist[i]['period'] == 'wet'])
        datalist2.append(datalist[i].loc[datalist[i]['period'] == 'dry'])
    datalist.clear()
    datalist3 = list()
    for i in range(len(datalist2)):
        datalist3.append(datalist2[i].sample(n=2, replace=True))

    length = len(datalist2)
    datalist2.clear()
    datalist4 = list()
    l = 0
    df.reset_index(inplace=True)
    longestduration = 0
    # from original dataframe extract out row with dates in the duration and put in different dataframe, each dataframe is a event
    for i in range(length):
        start_date = datalist3[i].iloc[0, 0]

        datalist3[i]['duration'] = datalist3[i]['duration'].astype(str).astype(int)
        durations = datalist3[i]['duration'].iloc[0]

        if longestduration < durations:
            longestduration = durations
        end_date = start_date + pd.Timedelta(days=durations)
        mask = (df[df.columns[0]] >= start_date) & (df[df.columns[0]] <= end_date)
        tempdata = df.loc[mask].copy()
        datalist4.append(tempdata)
        l = l + 1
        start_date = datalist3[i].iloc[1, 0]
        durations = datalist3[i]['duration'].iloc[1]
        if longestduration < durations:
            longestduration = durations
        end_date = start_date + pd.Timedelta(days=durations)
        mask = (df[df.columns[0]] >= start_date) & (df[df.columns[0]] <= end_date)
        tempdata = df.loc[mask].copy()
        datalist4.append(tempdata)
        l = l + 1

    # fill baseflow values and recalculate diff(discharge - baseflow)
    for i in range(length):
        start = datalist4[i].iloc[0, 0]
        dura = datalist3[i]['duration'].iloc[0]
        end = start + pd.Timedelta(days=dura)
        start_base = datalist4[i]['base'].iloc[0]
        end_base = datalist4[i]['base'].iloc[-1]

        # calculating gap
        if start_base > end_base:
            gap = (start_base - end_base) / dura

        if start_base < end_base:
            gap = (end_base - start_base) / dura

        # counter column
        for j in range(len(datalist4[i])):
            datalist4[i]['counter'] = 0
            for m in range(len(datalist4[i]['counter'])):
                datalist4[i]['counter'].iloc[m] = m

        for j in range(len(datalist4[i])):
            # replacing baseflow value 0 with gap
            datalist4[i]['base'] = [gap if x == 0 else x for x in datalist4[i]['base']]
            for m in range(len(datalist4[i]['base'])):
                if (datalist4[i]['base'].iloc[m] == gap):
                    # calculating new baseflow values
                    datalist4[i]['base'].iloc[m] = start_base + (
                                datalist4[i]['base'].iloc[m] * datalist4[i]['counter'].iloc[m])
                    # recalculating diff values
                    datalist4[i]['diff'].iloc[m] = datalist4[i]['Discharge (m3/s)'].iloc[m] - datalist4[i]['base'].iloc[
                        m]

    pcadf = DataFrame(index=np.arange(l), columns=np.arange(longestduration + 1))
    # convert dataframe of date and discharge to event to diffrences
    for i in range(l):
        series = datalist4[i]['diff']
        list1 = series.tolist()
        listlength = len(list1)
        pcadf.iloc[i, 0:listlength] = list1

    pcadf.fillna(0, inplace=True)
    pca = PCA(n_components=2)
    principalcomponent = pca.fit_transform(pcadf)
    principaldf = pd.DataFrame(data=principalcomponent, columns=['principal component 1', 'principal component 2'])
    return pcadf



