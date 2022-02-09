import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

def func(ticker):
    source = pdr.get_data_yahoo(ticker)
    day = np.arange(1, len(source) + 1)
    source.drop(columns=['Adj Close', 'Volume'], inplace=True)
    source['day'] = day
    source = source[['day', 'Open', 'High', 'Close', 'Low']]
    source['9-day'] = source['Close'].rolling(9).mean().shift()
    source['21-day'] = source['Close'].rolling(21).mean().shift()
    source['signal'] = np.where(source['9-day'] > source['21-day'], 1, 0)
    source['signal'] = np.where(source['9-day'] < source['21-day'], -1, source['signal'])
    source.dropna(inplace=True)
    source['return'] = np.log(source['Close']).diff()
    source['sys_return'] = source["signal"] * source['return']
    source['entry'] = source.signal.diff()
    df = pd.DataFrame(source)
    plt.cla()
    plt.rcParams['figure.figsize'] = 12, 6
    plt.grid(True, alpha=.3)
    plt.plot(source.iloc[-252:]['Close'], label=ticker)
    plt.plot(source.iloc[-252:]['9-day'], label='9-day')
    plt.plot(source.iloc[-252:]['21-day'], label='21-day')

    plt.plot(source[-252:].loc[source.entry == 2].index, source[-252:]['9-day'][source.entry == 2], '^',
            color='green', markersize=15)
    plt.plot(source[-252:].loc[source.entry == -2].index, source[-252:]['21-day'][source.entry == -2], 'v',
            color='red', markersize=15)
    plt.legend(loc=2)
    df = pd.DataFrame(np.exp(source['return']).cumprod(), np.exp(source['sys_return']).cumprod())
    return plt

