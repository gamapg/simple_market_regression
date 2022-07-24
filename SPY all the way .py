# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 03:17:16 2021

@author: Gama
"""

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import pandas_datareader.wb as wb
import numpy as np
from pandas_datareader import data as pdr

import yfinance as yf
start = dt.datetime(1999, 1, 1)
end = dt.datetime(2022, 1, 1)
gold_prices = pdr.get_data_yahoo("GC=F", start, end)
print(gold_prices)

crude_oil_prices = pdr.get_data_yahoo("CL=F",  start, end)
print(crude_oil_prices)


nasdaq_data = pdr.get_data_yahoo("NDX", start, end)
print(nasdaq_data)

sap_data = pdr.get_data_yahoo("SPY",  start, end)
print(sap_data)

###________________________________________________________

gdp_data = wb.download(indicator="NY.GDP.MKTP.CD", country="US", start =start, end=end)
print(gdp_data)
export_data = wb.download(indicator="NE.EXP.GNFS.CN", country="US", start =start, end=end)
print(export_data)

print("_____________________________________________")

def log_return(prices):
  return np.log(prices/prices.shift(1))

gold_returns = log_return(gold_prices["Gold_Price"])
crude_oil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
nasdaq_returns = log_return(nasdaq_data['NDX'])
sap_returns = log_return(sap_data['SPY'])
gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])
export_returns = log_return(export_data['NE.EXP.GNFS.CN'])


print(gold_returns.var())
print(crude_oil_returns.var())
print(nasdaq_returns.var())
print(sap_returns.var())
print(gdp_returns.var())
print(export_returns.var())