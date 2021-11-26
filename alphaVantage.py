from alpha_vantage.timeseries import TimeSeries

key = 'S0RLT7YD5ATL9UGK'
ts = TimeSeries(key)
aapl, meta = ts.get_intraday(symbol = 'AAPL', interval='1min', outputsize = 'full')
print(aapl['2021-11-25'])