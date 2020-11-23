
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
from sklearn.impute import SimpleImputer
from pandas import DataFrame

fig, ax = plt.subplots(figsize=(14, 10))
# canvas = FigureCanvasTkAgg(fig, master=root)
# plot_widget = canvas.get_tk_widget()

'''
# read xlsx files
# def open_file():
#file = askopenfile(mode='r', filetypes=[('xlsx files', '*.xlsx')])
#if file is not None:
    # print(file.name)
#read_file = pd.read_excel('Book3.xlsx')
#read_file.to_csv('Book3.csv', index=None, header=True)

#reading for s5 and s6  df= discharge df2= rainfall
    #df = pd.read_excel('Telok Buing Discharge.xlsx', index_col=0)
    #df['Discharge (m3/s)'] = df['Discharge (m3/s)'].astype('float64')
    #df.info()
    #print(df.dtypes)
'''
def baseflowdiagram(df):
    # figure s5
    df['Discharge (m3/s)'] = df['Discharge (m3/s)'].astype('float64')
    ax.bar(df.index.values, df['Discharge (m3/s)'],1.85)
    ax.set(xlabel ="Date/Time",ylabel = "Discharge(m3/s)",title = "Hydrograph")
    ax.set_xlim(min(df.index.values), max(df.index.values))
    # ax.set_ylim(0,max(df['Discharge (m3/s)']))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    dfd = df['Discharge (m3/s)']
    var = dfd[argrelextrema(dfd.to_numpy(dtype='float64', na_value=np.nan), np.less)[0]]
    var.interpolate()
    ax.plot(var.index.values,var, color='red')
    plt.legend()



def hydrograph_baseflow(df):
    # figure s6
    dframe = df.head(200)
    ax.plot(dframe.index.values, dframe['Discharge (m3/s)'],color='blue', linestyle='-')
    ax.set(xlabel ="Date/Time",ylabel = "Discharge(m3/s)",title = "Hydrograph")
    ax.set_xlim(min(dframe.index.values), max(dframe.index.values))
    # ax.set_ylim(0,max(df['Discharge (m3/s)']))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    df4 = dframe['Discharge (m3/s)']
    var1 = df4[argrelextrema(df4.to_numpy(dtype='float64', na_value=np.nan), np.less)[0]]
    var1.interpolate()
    ax.plot(var1.index.values,var1, color='red',label='baseflow')
    plt.legend()


def linear_regression(df,df2):
    # read and group discharge by month
    df[df.columns[0]]= pd.to_datetime(df[df.columns[0]])
    dataf= DataFrame(df.groupby(pd.Grouper(key=df.columns[0], freq='1M'))[df.columns[1]].mean())

    # compute the mean for each month the rainfall values of all  stations , put the mean in another col
    df2[df2.columns[0]]= pd.to_datetime(df2[df2.columns[0]])
    df2.set_index(df2.columns[0], inplace=True)
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

    #visualize
    plt.scatter(lx, ly)
    plt.plot(lx, yl, color='red')
    plt.legend()

    '''
    # plt.show()
   # fig.savefig('blah.png', transparent=True)

    # xvalue = pd.to_datetime(df[df.columns[0]])
       # yvalue = df.loc[df['Discharge (m3/s)']>5000.000000]
       # yvalue = yvalue.astype(np.float)
       # ax.bar(xvalue,yvalue)

       # for index , row in df.iterrows():
        #    print(index, row['Discharge (m3/s)'])
        #x = df['Date/Time']
        #y = df['Discharge (m3/s)']
        #df2 = df.loc[df['Discharge (m3/s)']>5000]
        #x1 = df2['Date/Time']
        #y1 = df2['Discharge (m3/s)']
        # print(type(y1))
        # bar chart
        # plt.bar(x1,y1, width=1)
        # plt.margins(0,0)
        # plt.title('baseflow diagram',fontdict={'fontsize':'13', 'color':'red'}, loc='left')
        # plt.xlabel('Date')
        # plt.ylabel('Discharge')

 tk.Button(root, text='Open', command=open_file).grid(row=2, column=1)


 def update():
    fig.canvas.draw()


 def _quit():
    root.quit()
    root.destroy()  # correction: to clean the window when exit

# def save():
    plt.savefig('mygrapgh.png',dpi=300)

plot_widget.grid(row=0, column=0)
# update button
tk.Button(root, text="Update", command=update).grid(row=1, column=0)
# quit button
tk.Button(root, text='Quit', command=_quit).grid(row=2, column=0)
# save button
tk.Button(root, text='Save', command=save).grid(row=2, column=2)

root.mainloop()
'''