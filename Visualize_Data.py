# Author: Richard
# DATE:2018/9/6
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

style.use('ggplot')


def visualize_data():
    df = pd.read_csv('SP500_Join_AdjClose.csv')

    df_corr = df.corr()
    df_corr.to_csv('SP500_Corr.csv')

    data1 = df_corr.values

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
    fig1.colorbar(heatmap1)

    ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
    ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)

    ax1.invert_yaxis()
    ax1.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index
    ax1.set_xticklabels(column_labels)
    ax1.set_yticklabels(row_labels)

    plt.xticks(rotation=90)
    heatmap1.set_clim(-1, 1)
    plt.tight_layout()
    plt.savefig("correlations.png", dpi = (300))
    plt.show()


visualize_data()
