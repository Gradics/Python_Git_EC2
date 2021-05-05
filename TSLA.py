# https://towardsdatascience.com/a-comprehensive-guide-to-downloading-stock-prices-in-python-2cd93ff821d4


import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

tsla_df = yf.download('TSLA', 
                      start='2021-01-01', 
                      progress=False)
#tsla_df.head()
tsla_df.tail()

#tsla_df['Close'].plot(title="TSLA's stock price")

