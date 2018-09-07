# Author: Richard
# DATE:2018/9/6
# -*- coding: utf-8 -*-


import pickle
import pandas as pd


def compile_data():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)[:60]

    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        df = pd.read_csv("stock_dfs/{}.csv".format(ticker))
        df.set_index("Date", inplace=True)
        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

    print(main_df.head())
    main_df.to_csv('SP500_Join_AdjClose.csv')


compile_data()
