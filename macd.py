import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filename = "Nirou.Moharreke.csv"


def process_file(name):
    df = pd.read_csv(name)
    df = df.rename(columns={"<DTYYYYMMDD>": "Date"})
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format="%Y%m%d")
    df = df.set_index(df['Date'].values)
    return df


def macd(df):
    # Macd
    S_term = 10
    L_term = 25
    s_ema = df.close.ewm(span=S_term, adjust=False).mean()
    l_ema = df.close.ewm(span=L_term, adjust=False).mean()
    # calculate MACD
    macd = s_ema - l_ema

    signal_term = 8
    signal_line = macd.ewm(span=signal_term, adjust=False).mean()
    return macd, signal_line

def plotting_graph(df, macd, signal_line):
    plt.figure(figsize=(12.2, 4.5))  # width = 12.2in, height = 4.5
    plt.plot(df.index, macd, label='Khmoharreke macd', color='red')
    plt.plot(df.index, signal_line, label='Signal Line', color='blue')
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')
    plt.show()

dataframe = process_file(filename)
macd, signal_line = macd(dataframe)
plotting_graph(dataframe, macd, signal_line)