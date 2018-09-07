# Author: Richard
# DATE:2018/9/4
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)

df['MA100'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['MA100'])
ax2.bar(df.index, df['Volume'])

plt.show()
