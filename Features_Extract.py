# Author: Richard
# DATE:2018/9/6
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from collections import Counter


def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('SP500_Join_AdjClose.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df


def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0


def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)]))

    # vals = df['{}_target'.format(ticker)].values.tolist()
    # str_vals = [str(i) for i in vals]
    # print('Data spread:', Counter(str_vals))

    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values  # The capital X contains our featuresets (daily % changes for every company in the S&P 500)
    y = df['{}_target'.format(ticker)].values   # The lowercase y is our "target" or our "label."

    return X, y, df


if __name__ == '__main__':
    extract_featuresets('MMM')
