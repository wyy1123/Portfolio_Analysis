import bs4
import requests
import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from grab_asset_data import daily_HLOCV

#the portfolioclass
class Portfolio():

    def __init__(self, stock_symbols, share_numbers):
        self.stock_symbols = stock_symbols
        self.share_numbers = share_numbers
        self.portfolio_value = 0
        self.stock_values = []
        self.stock_weights = []

    #a method that calculates the portfolio value on a certain date:
    def calc_portfolio_value(self,date):
        #to-do: figure out a way to set the start date dynamically
        start = dt.datetime(2000,1,1)
        # are there ways to make this more efficient?
        # e.g. ways to get the last stock price w/o grabbing the whole dataframe
        for i in range(len(self.stock_symbols)):
            df = daily_HLOCV(self.stock_symbols[i], start, date)
            #to-do: figure out a way to grab the stock price from the last trading day
            last_stock_price = df['Close'][date]
            self.stock_values.append(last_stock_price)

        self.portfolio_value = np.sum(np.asarray(self.stock_values))

        for i in range(len(self.stock_values)):
            self.stock_weights.append(self.stock_values[i]/self.portfolio_value)

    def visualize(self):
        labels = self.stock_symbols
        sizes = self.stock_weights

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  
        plt.show()





    

