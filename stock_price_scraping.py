import pandas_datareader as data

d = data.DataReader("AAPL", 'google', '2017-01-01', '2017-05-22')

print(d)
