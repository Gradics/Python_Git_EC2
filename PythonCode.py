import bt

# Download historical prices
bt_data = bt.get('fb, amzn, goog, nflx, aapl',
               start='2020-12-1', end='2020-12-31')
# Print the top five rows
print(bt_data.head(10))
