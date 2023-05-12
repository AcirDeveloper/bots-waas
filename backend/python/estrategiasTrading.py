# -*- coding: utf-8 -*-
"""
Created on Wed May 10 03:58:19 2023

@author: Acir
"""

# %% Librerías
import talib as ta
import matplotlib.pyplot as plt
import yfinance as yf

plt.style.use('bmh')

aapl = yf.download("AAPL", start="2019-01-01", end="2021-01-01")

# print(aapl)

# %% Medias móviles

aapl['SMA'] = ta.SMA(aapl.Close.values, 21)
aapl['EMA'] = ta.EMA(aapl.Close.values, 55)

# Plot

aapl[['Close', 'SMA', 'EMA']].plot(figsize=(15, 15))
plt.show()

# %% Bollinger Band

aapl['upper_band'], aapl['middle_band'], aapl['lower_band'] = ta.BBANDS(aapl['Close'], timeperiod=20)

# plot 

aapl[['Close', 'upper_band', 'middle_band', 'lower_band']].plot(figsize=(15, 15))

plt.show()

# %% RSI

aapl['RSI'] = ta.RSI(aapl.Close, 14)
aapl['RSI'].plot(figsize=(15, 15))

# plot

plt.show()