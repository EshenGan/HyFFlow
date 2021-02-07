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

packageNames = ('afex', 'emmeans','hydrostats')
utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)

packnames_to_install = [x for x in packageNames if not rpackages.isinstalled(x)]

# Running R in Python example installing packages:
if len(packnames_to_install) > 0:
    utils.install_packages(StrVector(packnames_to_install))
# loadpackage
hydrostat =importr('hydrostats')
#import
df=pd.read_excel("C:\\Users\\kumab\\Desktop\\main\\Telok Buing Discharge.xlsx")
df.columns=['Date','Q']
#convert from pandas format to r format
with localconverter(ro.default_converter + pandas2ri.converter):
  Colwell= ro.conversion.py2ri(df)
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
#print it out might need to test whether can be table or not
print(result)