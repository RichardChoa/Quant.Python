# Author: Richard
# DATE:2018/9/4
# -*- coding: utf-8 -*-


import pandas_datareader.data as web
import fix_yahoo_finance as yf
import datetime


yf.pdr_override()

start = datetime.datetime(2017, 9, 4)
end = datetime.datetime(2018, 9, 4)
data = web.get_data_yahoo("AEE", start, end)

print(data.head())

# data.to_csv('TSLA.csv', encoding='utf-8')
