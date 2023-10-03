import datetime
import yfinance as yf
import pandas as pd

yf.download("MSFT",period="6mo")

data = yf.download("MSFT", start="2023-01-01", end="2023-06-30")

# print(data.head())

# print(data.describe())

print(data.columns)

print(data['Close'])

# data = yf.download("MSFT", period='1mo', interval="5m")


