# Author: Richard
# DATE:2018/9/5
# -*- coding: utf-8 -*-


import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import fix_yahoo_finance as yf
import pickle
import requests
import time


yf.pdr_override()


def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    return tickers


# save_sp500_tickers()


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2017, 9, 4)
    end = dt.datetime(2018, 9, 4)

    # i = 0
    # while i <= len(tickers):
    #     if not os.path.exists('stock_dfs/{}.csv'.format(tickers[i])):
    #         df = web.get_data_yahoo(tickers[i], start, end)
    #         df.to_csv('stock_dfs/{}.csv'.format(tickers[i]))
    #         time.sleep(0.5)
    #     else:
    #         print('Already have {}'.format(tickers[i]))
    #     i = i + 1

    for ticker in tickers:     # for ticker in tickers[:10] if just need to do 10 times
        # just in case your connection breaks, we'd like to save our progress!
        try:
            if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
                df = web.get_data_yahoo(ticker, start, end)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
                print("{}.csv created".format(ticker))
                time.sleep(0.5)
            else:
                print('Already have {}'.format(ticker))
        except Exception:
            continue

    print('Mission Completed')


get_data_from_yahoo()
