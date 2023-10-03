import datetime
import yfinance as yf
import pandas as pd

# create list of stocks
stocks = ["AMZN", "MSFT", "GOOG", "D05.SI" ]
start = datetime.datetime.today() - datetime.timedelta(30)
end = datetime.datetime.today()

cl_price = pd.DataFrame() # closing prices

ohlcv_data = {}

# loop over tickers
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
    print(cl_price[ticker])

for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker, start, end)

print(ohlcv_data["D05.SI"]["Open"])




