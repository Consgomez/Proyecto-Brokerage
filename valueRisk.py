from numpy.core.fromnumeric import std
import yfinance as yf
import numpy as np
from scipy.stats import norm
from tabulate import tabulate

# daily = yf.download('MXN=X', '2020-01-01', '2021-11-24')
# daily = daily[['Close']]
# daily['returns'] = daily.Close.pct_change()
# print(daily)

# mean = np.mean(daily['returns'])
# std_dev = np.std(daily['returns'])

# var_90 = norm.ppf(1-0.9, mean, std_dev)
# var_95 = norm.ppf(1-0.95, mean, std_dev)
# var_99 = norm.ppf(1-0.99, mean, std_dev)

# print(tabulate([['90%', var_90], ['95%', var_95], ['99%', var_99]], headers=['Confidence Level', 'Value at Risk']))

ticker = yf.Ticker("aapl")
print(ticker.info['currentPrice'])