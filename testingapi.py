
import pandas
from time import sleep
import yfinance as yf

sleep(1)

#get stock code and period
stock = str(input('Please name the stock code:  '))
period = str(input('What time interval do you want the prediction to be based on? (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max):  '))

stock_info = yf.Ticker(stock)   #retrieves stock info
historical = stock_info.history(period=period)  #historical data for a given period
print("Maximum Closing Price: {0}".format(max(historical.Close)))
print("Minimum Closing Price: {0}".format(min(historical.Close)))
print(historical)


historical_dataframe = pandas.DataFrame(historical, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'])
price_august282000 = historical_dataframe.Close[historical_dataframe.Date  == "2000-08-28"]

print(price_august282000)

