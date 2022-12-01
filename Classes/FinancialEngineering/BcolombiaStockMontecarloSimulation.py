from tkinter import Tk, Label, Button

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


BcmbiaData = pd.read_csv('Classes/FinancialEngineering/Bancolombia.csv',header=0, usecols=['Date', 'Close'],parse_dates=True,index_col='Date')
print(BcmbiaData.info())
print(BcmbiaData.head())
print(BcmbiaData.tail())
print(BcmbiaData.describe())

plt.figure(figsize=(10,5))
plt.plot(BcmbiaData)
plt.show()

BcmbiaDataPctChange = BcmbiaData.pct_change()

BcmbiaLogReturns = np.log(1 + BcmbiaDataPctChange) 
print(BcmbiaLogReturns.tail(10))

plt.figure(figsize=(10,5))
plt.plot(BcmbiaLogReturns)
plt.show()

MeanLogReturns = np.array(BcmbiaLogReturns.mean())

VarLogReturns = np.array(BcmbiaLogReturns.var()) 

StdevLogReturns = np.array(BcmbiaLogReturns.std()) 


Drift = MeanLogReturns - (0.5 * VarLogReturns)
print("Drift = ",Drift)

NumIntervals = 6239

Iterations = 27

np.random.seed(7)
SBMotion = norm.ppf(np.random.rand(NumIntervals, Iterations))



DailyReturns = np.exp(Drift + StdevLogReturns * SBMotion)


StartStockPrices = BcmbiaData.iloc[0]

StockPrice = np.zeros_like(DailyReturns)

StockPrice[0] = StartStockPrices

for t in range(1, NumIntervals):

    StockPrice[t] = StockPrice[t - 1] * DailyReturns[t]
    


plt.figure(figsize=(10,5))

plt.plot(StockPrice)   

BcmbiaTrend = np.array(BcmbiaData.iloc[:, 0:1])

plt.plot(BcmbiaTrend,'k*')   

plt.show()
 