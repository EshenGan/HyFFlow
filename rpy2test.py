import rpy2.robjects as robjects
import pandas as pd
import rpy2.robjects.packages as rpackages
import rpy2.robjects as ro

from rpy2.robjects.vectors import StrVector
from pandas import DataFrame
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import importr
from pandas.core.index import Index as PandasIndex

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_pdf import PdfPages
from tkinter import filedialog
import tkinter as tk

import matplotlib.pyplot as plt

def colwelstep(df):
        df.columns=['Date','Q']
            #convert from pandas format to r format
        with localconverter(ro.default_converter + pandas2ri.converter):
            Colwell= ro.conversion.py2rpy(df)
            #create r global variable Colwell and result
        robjects.globalenv['Colwell'] = Colwell
        robjects.globalenv['result'] =0
            #use robject to run r script
        robjects.r(
            'Colwell <- as.data.frame(Colwell) '
        )
            #use robject to run r script
        robjects.r(
            'result=Colwells(Colwell, boundaries="weighted_log_class_size", s=12,indices.only=TRUE)'
        )
            #get the result from global variable
        result=robjects.globalenv['result']
        return result
        
def cw_indices(df):
    ax = plt.subplot()
    ax.axis('off')
    ax.set_title('Colwell Indices')

    packageNames = ('afex', 'emmeans','hydrostats')
    utils = rpackages.importr('utils')
    utils.chooseCRANmirror(ind=1)

    packnames_to_install = [x for x in packageNames if not rpackages.isinstalled(x)]

    #     # Running R in Python example installing packages:
    if len(packnames_to_install) > 0:
        utils.install_packages(StrVector(packnames_to_install))
        # loadpackage
    hydrostat =importr('hydrostats')
        #import
    # df=pd.read_excel(r"D:\UNMC\CSAI Year 2\Software Engineering Group Project\Project Documents\Telok Buing Discharge.xlsx")

        #storing values in dataframe to create table
    result=colwelstep(df)
    df1 = pd.DataFrame(result, columns = ['result'], dtype = float)

    lst = [[df1.result[0], df1.result[1], df1.result[2], df1.result[3], df1.result[4]]]

    df2 = pd.DataFrame(lst, columns = ['P', 'C', 'M', 'CP', 'MP'], index = ['Results'], dtype = float)

    table = ax.table(cellText = df2.values, colLabels = df2.columns, loc = 'center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.2,2.5)

