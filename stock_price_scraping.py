import pandas_datareader as data

DATA_SOURCE = 'google'

def getStockDate(ticker, start_date, end_date):
    return data.DataReader(ticker, DATA_SOURCE, start_date, end_datec)
