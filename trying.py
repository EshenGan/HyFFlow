import tkinter as tk
import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfile

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters

from cal_return import calculate_return2

def _pandas_converters():
    converters_active = check_if_active()  # something like pd.Timestamp in matplotlib.units.registry
    pd.plotting.deregister_matplotlib_converters()
    yield
    if converters_active:
        pd.plotting.register_matplotlib_converters()


root = tk.Tk()

fig, ax = plt.subplots(figsize=(15,6))
t = np.arange(0.0,3.0,0.01)
s = np.sin(np.pi*t)
plt.plot(t,s)

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

# read csv files
def open_file():
    file = askopenfile(mode='r', filetypes = [('xlsx files', '*.xlsx')])
    if file is not None:
        print(file.name)
        data = pd.read_excel(file.name)
        
        plt.clf() # clear plot first
        data[data.columns[0]]=pd.to_datetime(data[data.columns[0]])
        #dg = data.groupby(pd.Grouper(key='Time', freq='1W')).sum()#way to group by week
        data['months'] = data[data.columns[0]].apply(lambda x:x.strftime('%B'))#add new row month with month name January etc
        data['year'] = pd.DatetimeIndex(data[data.columns[0]]).year
        data_annualmax=data.groupby(data['year']).max()




        data_dischargesorted=calculate_return2(data,data.columns[1])
        df=data.groupby(pd.Grouper(key=data.columns[0], freq='1M'))[data.columns[1]].mean()
        df=df.rolling(10,1).mean()
        
        #try1=plt.plot(data.groupby(pd.Grouper(key=data.columns[0], freq='1M'))[data.columns[1]].mean(),'g-', label='median')#plot monthly mean
        #try2=plt.plot(data.groupby(pd.Grouper(key=data.columns[0], freq='1M'))[data.columns[1]].mean().rolling(12).mean(),'r', label='moving average')#plot moving average 
        #plt.legend()
        #plt.xlabel('Date/Time')
        #plt.ylabel('Water Discharge (m/s)')
       # for group in groupped:
          # plt.plot(group['probability'],group[data_dischargesorted.columns[2]],)
        
        df2=data_dischargesorted.sort_values(by= data_dischargesorted.columns[2],ascending=False)
        colum=df2[df2.columns[2]]
        data_dischargesorted['descending discharge']=colum
        #print(data_dischargesorted)
        plt.plot(data_dischargesorted['exceeding probability'],colum,color='grey',label="Daily Mean Calculated")
        plt.xlabel('exceeding probability')
        plt.ylabel('Discharge')
        plt.xlim(0,100)
        plt.title("Annual Flow duration")
#         try1=plt.plot(x, y,'g',label='Count')
#         plt.xlabel('Time')
#         plt.ylabel('Count')
#         ax2=plt.twinx()
#         try2=ax2.plot(x,z,'b' ,label='Water Discharge')
#         try3=ax2.plot(x,z.rolling(3).mean(),'b' ,label='Water Discharge moving avverage')
#         ax2.set_ylabel('Water Discharge')
#         plt.xticks(x[::3])
#         leg=try1+try2+try3
#         labs=[l.get_label() for l in leg]
#         ax2.legend(leg, labs, loc=0)
        # plt.draw()
        # fig.canvas.draw() 
 

tk.Button(root, text='Open', command = open_file).grid(row=2, column=1)

def update():
    fig.canvas.draw() 

def _quit():
    root.quit()
    root.destroy()  # correction: to clean the window when exit

plot_widget.grid(row=0, column=0)
tk.Button(root,text="Update",command=update).grid(row=1, column=0)

# add a quit button below 'update' button
tk.Button(root, text = 'Quit', command = _quit).grid(row=2, column=0)

root.mainloop()