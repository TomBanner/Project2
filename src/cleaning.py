import yfinance as yf
import pandas as pd
from pandas import json_normalize

import requests 
import json
import os
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import seaborn as sns



def importing():
    sp500 = yf.Ticker('^GSPC')
    sp500_hist = sp500.history(start="2013-04-29", end="2021-07-06")
    sp500_hist.to_csv('sp500.csv')
    df=pd.read_csv('sp500.csv')
    return df


def importcsv():
    df2 = pd.read_csv("/Users/tom/desktop/Project2/coin_Bitcoin.csv")
    return df2



def datecleaner(df):
    df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.date
    return df




def columncleaner(df):
    df[['Date', 'Open', 'High', 'Low', 'Close']]
    return df