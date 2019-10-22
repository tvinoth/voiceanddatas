# AR example
from statsmodels.tsa.ar_model import ARMA
from random import random
# contrived dataset
# data = [x + random() for x in range(1, 100)]
# print(data)
# # fit model
# model = AR(data)
# model_fit = model.fit()
# # # make prediction
# yhat = model_fit.predict(len(data), len(data))
# print(yhat)

data = [x + random() for x in range(1, 100)]
# fit model
model = ARMA(data, order=(0, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)