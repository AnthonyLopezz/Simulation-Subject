import datetime as dt
import numpy as np
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

StockList = ['BOGOTA.CL', 'BCOLOMBIA.CL'] 
StartDay = dt.datetime(2019, 1, 1)
EndDay = dt.datetime(2019, 12, 31)

StockData =  wb.DataReader(StockList, 'yahoo',StartDay,EndDay)
StockClose = StockData["Adj Close"]
print(StockClose.describe())

fig, axs = plt.subplots(2, 1)
axs[0].plot(StockClose['BOGOTA.CL'])
axs[0].set_title('BANCO DE BOGOTÁ')
axs[1].plot(StockClose['BCOLOMBIA.CL'])
axs[1].set_title('BANCOLOMBIA')

plt.figure(figsize=(10,5))
plt.plot(StockClose)
plt.subplot_tool()
plt.show()

StockReturns = StockClose.pct_change()
print(StockReturns.tail(15))

PortvolioValue = 1000000000.00
ConfidenceValue = 0.95
MeanStockRet = np.mean(StockReturns)
StdStockRet = np.std(StockReturns)

WorkingDays2019 = 252.
AnnualizedMeanStockRet = MeanStockRet/WorkingDays2019
AnnualizedStdStockRet = StdStockRet/np.sqrt(WorkingDays2019)

INPD = norm.ppf(1-ConfidenceValue,AnnualizedMeanStockRet,AnnualizedStdStockRet)
VaR = PortvolioValue*INPD

RoundVaR=np.round_(VaR,2)

for i in range(len(StockList)):
    print("Value-at-Risk for", StockList[i], "is equal to ",RoundVaR[i])
