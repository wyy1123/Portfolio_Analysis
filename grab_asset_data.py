import bs4
import requests
import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
import pandas_datareader.data as web
# from bs4 import BeautifulSoup


# def cur_price(tick_symbol):
#     r = requests.get('https://finance.yahoo.com/quote/'+tick_symbol+'?p='+tick_symbol)
#     soup = bs4.BeautifulSoup(r.text,"xml")
#     price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
#     return price

#daily_HLOCV returns a dataframe of HLOCV of a stock during the desired period
def daily_HLOCV(tick_symbol, start, end): 
    style.use('ggplot')
    # start = dt.datetime(2000,1,1)
    # end = dt.datetime(2019,8,20)
    df = web.DataReader(tick_symbol,'yahoo', start, end)
    return df