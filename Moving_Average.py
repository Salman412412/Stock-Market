# -*- coding: utf-8 -*-
"""
@author: Omid
@python_version: 3.8
"""

import pandas as pd

def read_file(filename=None):
    df = pd.read_csv(filename)
    df = df.rename(columns={"<DTYYYYMMDD>": "Date"})
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format="%Y%m%d")
    #seting index for graph
    df = df.set_index(df['Date'].values)
    df = df.iloc[::-1] #reverse because of dates!
    #drop rows that have 0 amounts!
    zero = df.index[df['<VOL>'] == 0].tolist()
    for i in range(len(zero)):
        df = df.drop(zero[i])
    return df

def SMA(df, sdays):
    sma_list = df['<LAST>']
    sma_list = sma_list.iloc[::-1]
    sma = pd.Series(sma_list.rolling(sdays).mean())
    df['SMA'] = sma
    return df

def EMA(df, edays):
    ema_list = df['<LAST>']
    ema_list = ema_list.iloc[::-1]
    ema = pd.Series(ema_list.ewm(span=edays, adjust=False, min_periods= edays-1).mean())
    df['EMA'] = ema
    return df


if __name__ == "__main__":
    filename = _csvfile_  # put csv file address
    n_days = 20  # number of days

    dataframe = read_file(filename)
    dataframe_ma = SMA(dataframe, n_days)
    dataframe_ema = EMA(dataframe_ma, n_days)













