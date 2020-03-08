import requests
import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from grab_asset_data import daily_HLOCV

from grab_asset_data import daily_HLOCV
from portfolio import Portfolio

stock_symbols = ['TSLA','AAPL']
share_numbers = [1,1]
portfolio = Portfolio(stock_symbols,share_numbers)
 
date = start = dt.datetime(2020,3,6)

portfolio.calc_portfolio_value_on_date(date)

benchmark = '^GSPC'
portfolio.calc_portfolio_beta(benchmark)

print(portfolio.stock_values)
print(portfolio.stock_weights)
print(portfolio.stock_betas)
print(portfolio.portfolio_beta)

portfolio.visualize()