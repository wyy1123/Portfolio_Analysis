import requests
import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from grab_asset_data import daily_HLOCV


def stock_beta(stock_symbol,benchmark):
    start = dt.datetime(2000,1,1)
    end = dt.datetime.now()
    stock_df = daily_HLOCV(stock_symbol,start,end)

    stock_start = stock_df.index[0]
    stock_end = stock_df.index[-1]
    benchmark_df = daily_HLOCV(benchmark,stock_start,stock_end)

    stock_close = stock_df['Close']
    benchmark_close = benchmark_df['Close']

    #https://stackoverflow.com/questions/15317822/calculating-covariance-with-python-and-numpy
    cov_mat = np.cov(stock_close, benchmark_close)
    beta = cov_mat[0,1]/cov_mat[1,1]
    #to-do: fix the error: this version returns an error when stock
    #has an earlier start data than then benchmark does
    return beta








