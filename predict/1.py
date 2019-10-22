#to plot within notebook
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from dateutil.parser import parse
#from pyramid.arima import auto_arima
from pmdarima.arima import auto_arima

#setting figure size
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10
#for normalizing data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

#read the file
df = pd.read_csv('../NSE-TATAGLOBAL11.csv')
df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index = df['Date']
#plot
# plt.figure(figsize=(16,8))
# plt.plot(df['Close'], label='Close Price history')
# plt.show()

data = df.sort_index(ascending=True, axis=0)
train = data[:987]
valid = data[987:]
training = train['Close']
validation = valid['Close']
model = auto_arima(training, start_p=1, start_q=1,max_p=3, max_q=3, m=12,start_P=0, seasonal=True,d=1, D=1, trace=True,error_action='ignore',suppress_warnings=True)
model.fit(training)
forecast = model.predict(n_periods=248)
forecast = pd.DataFrame(forecast,index = valid.index,columns=['Prediction'])
plt.plot(train['Close'])
plt.plot(valid['Close'])
plt.plot(forecast['Prediction'])
plt.show()