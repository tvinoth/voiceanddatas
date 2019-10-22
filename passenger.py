from dateutil.parser import parse
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt #%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
from statsmodels.tsa.stattools import adfuller

# data = pd.read_csv('AirPassengers.csv')
# print(data.head())
# #print '\n Data Types:'
# print(data.dtypes)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
print(data.head())
print(data.index)

ts = data["#Passengers"].head(10)
#range
#ts['1949-01-01':'1949-05-01']
#ts[:'1949-05-01'] this is end value it will return from anything then this end

# print(ts)

# plt.plot(data)
# plt.show()
ts_log = np.log(ts)
plt.plot(ts_log)
# moving_avg = pd.rolling_mean(ts_log,12)
moving_avg = ts_log.rolling(12).mean()
moving_std = ts_log.rolling(12).std()

plt.plot(ts_log)
plt.plot(ts, color='blue',label='Original')
plt.plot(moving_avg, color='red')
plt.plot(moving_std, color='black', label = 'Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
plt.show()

# def test_stationarity(timeseries):
    
#     #Determing rolling statistics
#     ts_log = np.log(timeseries)
#     plt.plot(ts_log)
#     rolmean = ts_log(12).mean()
#     rolstd = ts_log(12).std()

#     #Plot rolling statistics:
#     orig = plt.plot(timeseries, color='blue',label='Original')
#     mean = plt.plot(rolmean, color='red', label='Rolling Mean')
#     std = plt.plot(rolstd, color='black', label = 'Rolling Std')
#     plt.legend(loc='best')
#     plt.title('Rolling Mean & Standard Deviation')
#     plt.show(block=False)

# test_stationarity(ts)



    
    #Perform Dickey-Fuller test:
    
    # dftest = adfuller(timeseries, autolag='AIC')
    # dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    # for key,value in dftest[4].items():
    #     dfoutput['Critical Value (%s)'%key] = value
    # print(dfoutput)