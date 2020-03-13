"""
Created on Fri Mar 13 16:54:56 2020
@author: Linji Wang (wang1278)
File Name: program-08
Description: 
Read contents of the file WabashRiver_DailyDischarge_20150317-20160324.txt
into a Pandas dataframe and do some data processing and plotting
"""

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
# Import data, use col 3,4 for datetime and col 6 for discharge(cfs)
data=pd.read_table('WabashRiver_DailyDischarge_20150317-20160324.txt',delimiter='\t',skiprows=25)
data.columns=['agency','site_no','dt','tz','Discharge(cfs)','si']
data['datetime']=pd.to_datetime(data['dt']+' '+data['tz'])
data.index=data['datetime']
data=data.drop(columns=['datetime','agency','site_no','dt','tz','si'])
# Plot for daily average streamflow
DailyAverageQ=data.resample('D').mean()
DailyAverageQ.plot(figsize=(10,10))
plt.title('Daily Average Streamflow')
plt.xlabel('Datetime')
plt.ylabel('Discharge(cfs)')
plt.savefig('DailyAverageStreamflow.pdf')
# Identify and plot the 10 days with highest flow and plot it on the same datetime scale
HQ_scaled=DailyAverageQ.nlargest(10,['Discharge(cfs)'])
plot1=DailyAverageQ.plot(figsize=(10,10))
plot2=plt.scatter(HQ_scaled.index,HQ_scaled['Discharge(cfs)'],color='r',label='Highest 10 Flow')
plot1.legend()
plt.title('Daily Average Streamflow with Highest 10 Flow')
plt.xlabel('Datetime')
plt.ylabel('Discharge(cfs)')
plt.savefig('DailyAverageStreamflowWithHighest10Flow.pdf')
# Calculate and plot monthly average streamflow
MonthlyAverageQ=data.resample('M').mean()
MonthlyAverageQ.plot(figsize=(10,10))
plt.title('Monthly Average Streamflow')
plt.xlabel('Datetime')
plt.ylabel('Discharge(cfs)')
plt.savefig('MonthlyAverageStreamflow.pdf')