# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 03:17:16 2021

@author: Gama
"""
import math 
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
import pandas_datareader.wb as wb
import numpy as np
from pandas_datareader import data as pdr

import yfinance as yf
start = datetime(1990, 1, 1)
end = datetime(2022, 2, 1)
gold_prices = pdr.get_data_yahoo("GC=F", start, end)
print(gold_prices)


crude_oil_prices = pdr.get_data_yahoo("CL=F",  start, end)
print(crude_oil_prices)


nasdaq_data = pdr.get_data_yahoo("^IXIC", start, end)
print(nasdaq_data)

sap_data = pdr.get_data_yahoo("^GSPC",  start, end)
print(sap_data)

vix_price = pdr.get_data_yahoo("^VIX", start, end)
print(vix_price)

###________________________________________________________

gdp_data = wb.download(indicator="NY.GDP.MKTP.CD", country="US", start =start, end=end)
print(gdp_data)
export_data = wb.download(indicator="NE.EXP.GNFS.CN", country="US", start =start, end=end)
print(export_data)

print("_____________________________________________")

def log_return(prices):
  return np.log(prices/prices.shift(1))

gold_returns = log_return(gold_prices["Adj Close"])
crude_oil_returns = log_return(crude_oil_prices['Adj Close'])
nasdaq_returns = log_return(nasdaq_data['Adj Close'])
sap_returns = log_return(sap_data['Adj Close'])
gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])
export_returns = log_return(export_data['NE.EXP.GNFS.CN'])
vix_returns = log_return(vix_price["Adj Close"])

print("Below are the variance of the log returns")
print("Gold_returns " + str(gold_returns.var()))
print("Crude Oil Returns " + str(crude_oil_returns.var()))
print("Nasdaq returns " + str(nasdaq_returns.var()))
print("S&P 500 Reutrnrs "+ str(sap_returns.var()))
print("GDP Reutrns "+ str(gdp_returns.var()))
print("Export returns " + str(export_returns.var()))
print("Vix returns "+ str(vix_returns.var()))
print("")
print("Below are the Standard deviation of the log returns")
print("Gold Returns " + str(gold_returns.std()))
print("Crude Oil Returns " + str(crude_oil_returns.std()))
print("NASDAQ Returns " + str(nasdaq_returns.std()))
print("S&P500 Returns " + str(sap_returns.std()))
print("GDP Reutrns " + str(gdp_returns.std()))
print("Export reutrns " + str(export_returns.std()))
print("Vix returns " + str(vix_returns.std()))