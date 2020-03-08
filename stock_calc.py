import requests
import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from grab_asset_data import daily_HLOCV

class Stock():
    def __init__(self, stock_symbol):
        self.symbol = stock_symbol
        self.daily_HLOCV = daily_HLOCV(stock_symbol,dt.datetime(2000,1,1), dt.datetime.now())
        self.closing_price_history = self.daily_HLOCV['Close']
        self.last_closing_price = self.closing_price_history[-1]
        self.sigma = 0
        self.beta = 0 

    def calc_beta(self, benchmark):
        #here the beta is calculated with price series since IPO
        stock_df = self.daily_HLOCV

        stock_start = stock_df.index[0]
        stock_end = stock_df.index[-1]
        benchmark_df = daily_HLOCV(benchmark,stock_start,stock_end)

        stock_close = stock_df['Close']
        benchmark_close = benchmark_df['Close']

        #https://stackoverflow.com/questions/15317822/calculating-covariance-with-python-and-numpy
        cov_mat = np.cov(stock_close, benchmark_close)
        beta = cov_mat[0,1]/cov_mat[1,1]
        #to-do:returns an error message instead of breaking down when stock
        #has an earlier start data than then benchmark does
        return beta


    def calc_sigma(self,start,end):
        stock_df = web.DataReader(self.ymbol,'yahoo', start, end)
        stock_sigma = np.std(stock_df['Close'])
        return stock_sigma


# start = dt.datetime(2000,1,1)
# end = dt.datetime(2020,3,7)

# print(stock_sigma('^GSPC',start,end))






