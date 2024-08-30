# Installing Yahoo Finance library
pip install yfinance

# importing libraries
import yfinance as yf
import pandas as pd

equity_details = pd.read_csv("EQUI.csv")
equity_details

for name in equity_details.SYMBOL:
  try:
    data = yf.download(f'{name}.NS', start="2015-01-01", end="2024-06-30")
    data.to_csv(name+".csv")
  except Exception as e:
    print(f'{name}.NS',e)
    continue

    print(name)
