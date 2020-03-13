"""
Linji Wang
PandasDateDemo.py
Tutorial code for time series analysis with pandas
03/13/19
"""

# import necessary modules
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
pd.set_option('display.max_rows',15)
pd.__version__
# Download data !wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii
# Load data
ao=np.loadtxt('monthly.ao.index.b50.current.ascii')
ao[0:2]
ao.shape
# Convert data into time series
dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M')
dates.shape
AO = Series(ao[:,2], index=dates)
AO
# plot the timeseries
AO.plot()
AO['1980':'1990'].plot()
AO['1980-05':'1981-03'].plot()
# Get numbers by number or index
AO[120]
AO['1960-01']
AO['1960']
AO[AO>0]

# Downloaded new data !wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/pna/norm.nao.monthly.b5001.current.ascii
# Create Series following the same procedures
nao=np.loadtxt('norm.nao.monthly.b5001.current.ascii')
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)
NAO.index
# Create dataframe taht contains both AO and NAO data
aonao=DataFrame({'AO':AO,'NAO':NAO})
# Plot the dataframe
aonao.plot(subplots=True)
# Call data from dataframe using different methods
aonao.head()
aonao['NAO']
aonao.NAO
# Add a column for differences
aonao['Diff'] = aonao['AO'] - aonao['NAO']
aonao.head()
# Delete column
del aonao['Diff']
aonao.tail
# Slicing
aonao['1981-01':'1981-03']
import datetime
aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) 
        & (aonao.index > datetime.datetime(1980,1,1)) 
        & (aonao.index < datetime.datetime(1989,1,1)),
        'NAO'].plot(kind='barh')
# Dataframe statistics
aonao.mean()
aonao.max()
aonao.min()
aonao.mean(1)
aonao.describe()
# Resampling
AO_mm=AO.resample('A').mean()
AO_mm.plot(style='g--')
AO_mm=AO.resample('A').median()
AO_mm.plot()
AO_mm = AO.resample("3A").apply(np.max)
AO_mm.plot()
AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
AO_mm['1900':'2020'].plot(subplots=True)
AO_mm['1900':'2020'].plot()
AO_mm
# Moving statistics
aonao.rolling(window=12,center=False).mean().plot(style='-g')
aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g')
aonao.corr()
