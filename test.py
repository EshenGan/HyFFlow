import unittest
import pandas as pd
import colwelselectsta as cs
import rpy2test as rp

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


class TestStringMethods(unittest.TestCase):
    #setup
    packageNames = ('afex', 'emmeans','hydrostats')
    utils = rpackages.importr('utils')
    utils.chooseCRANmirror(ind=1)

    packnames_to_install = [x for x in packageNames if not rpackages.isinstalled(x)]

    #     # Running R in Python example installing packages:
    if len(packnames_to_install) > 0:
        utils.install_packages(StrVector(packnames_to_install))
        # loadpackage
    hydrostat =importr('hydrostats')

    def testsplit(self):
        df=pd.read_excel(r'C:\Users\kumab\OneDrive\Desktop\main\monthlyrainfall.xlsx')
        data=cs.colwellsplit(df,1)

        self.assertEqual(data.columns[1],df.columns[1])
    
    def testmean(self):
        df=pd.read_excel(r'C:\Users\kumab\OneDrive\Desktop\main\monthlyrainfall.xlsx')
        data=cs.colwellforall(df)
        df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
        df['mean'] = df.mean(axis=1)
        row1=data.iloc[1,0]
        row1d=df.iloc[1,0]
        self.assertEqual(row1,row1d)

    def testresult(self):
        df=pd.read_excel(r'C:\Users\kumab\OneDrive\Desktop\main\monthlyrainfall.xlsx')
    
        datamean=cs.colwellforall(df)
        data=datamean.copy()
        result1=rp.colwelstep(data)
        #standardise the result in dataframe
        test1 = pd.DataFrame(result1, columns = ['result'], dtype = float)
        lst = [[test1.result[0], test1.result[1], test1.result[2], test1.result[3], test1.result[4]]]
        test2 = pd.DataFrame(lst, columns = ['P', 'C', 'M', 'CP', 'MP'], index = ['Results'], dtype = float)

        ######################
        #r steps
        datamean.columns=['Date','Q']
            #convert from pandas format to r format
        with localconverter(ro.default_converter + pandas2ri.converter):
            Colwell= ro.conversion.py2rpy(datamean)
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
        df1 = pd.DataFrame(result, columns = ['result'], dtype = float)
        lst = [[df1.result[0], df1.result[1], df1.result[2], df1.result[3], df1.result[4]]]
        df2 = pd.DataFrame(lst, columns = ['P', 'C', 'M', 'CP', 'MP'], index = ['Results'], dtype = float)
        self.assertEqual(test2.iloc[0,0],df2.iloc[0,0])

    
if __name__ == '__main__':
    unittest.main()
