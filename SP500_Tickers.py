# Author: Richard
# DATE:2018/9/5
# -*- coding: utf-8 -*-


import bs4 as bs
import pickle
import requests
import pandas as pd


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


tickers = save_sp500_tickers()
frame = pd.DataFrame(tickers, index=range(1, len(tickers)+1), columns=['Ticker'])
frame.to_csv('SP500_Tickers.csv', encoding='utf-8')
