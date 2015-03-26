import datetime
import pandas as pd
import pandas.io.data
from pandas import DateFrame
import matplotlib.pyplot as plt

sp500 = pd.io.data.get_data_yahoo('%5EGSPC', start = datetime.datetime(2000,10,1),
                                             end = datetime.datetime(2012,1,1))

print sp500.head() 
