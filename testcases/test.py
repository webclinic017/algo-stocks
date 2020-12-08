import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

METHOD_MODULE_PATH = os.path.abspath('..')
sys.path.insert(1, METHOD_MODULE_PATH)
import method.SaleRules as _sr
import method.algofuncs as _af


DATA_PATH = os.path.abspath('../vn-stock-data/VNX/')
ticker_data = _af.get_pricing_by_path(DATA_PATH + '/' + 'KOS.csv', start_date='2020-10-01')

mmi_week = _af.MMI(ticker_data["Close"], 5)
plt.figure()
plt.subplot(211)
plt.plot(ticker_data["Close"], label='Close Price', color='black')
plt.subplot(212)
plt.plot(mmi_week, label='MMI Week')
plt.legend()
plt.show()

# plt.figure()
# plt.subplot(211)
# Vol = _af.getVolatility(ticker_data["Close"], 252)
# # Vol2 = ticker_data["High"] - ticker_data["Low"]
# plt.plot(ticker_data["Close"], label='Close Price', color='black')
# plt.plot(ticker_data["High"], label='High Price')
# plt.plot(ticker_data["Low"], label='Low Price')
# plt.legend()
# plt.subplot(212)
# plt.plot(Vol, label='Volatility')
# plt.legend()
# plt.show()

# plt.plot(ticker_data["High"], label='High Price', linestyle = 'dotted')
# plt.plot(ticker_data["Low"], label='Low Price', linestyle = 'dotted')
# plt.legend()
# plt.show()

# Vol = ticker_data["High"] - ticker_data["Low"]
# print(Vol.tail())
# plt.plot(Vol, label='Volatility')
# plt.legend()
# plt.show()

## Computing Volatility
# Compute the logarithmic returns using the Closing price
# ticker_data['Log_Ret'] = np.log(ticker_data['Close'] / ticker_data['Close'].shift(1))
# Compute Volatility using the pandas rolling standard deviation function
# ticker_data['Volatility'] = ticker_data['Log_Ret'].rolling(window=252).std() * np.sqrt(252)
# Plot the ticker_data Price series and the Volatility
# ticker_data[['Close', 'Volatility']].plot(subplots=True, color='blue',figsize=(8, 6))
# plt.figure()
# plt.subplot(211)
# plt.plot(ticker_data[['Close']])
# plt.subplot(212)
# plt.plot(ticker_data[['Volatility']])
# plt.show()



# a = range(10, 35, 5)
# for n in a:
#   print(n)


# print(ticker_data)
# print(type(ticker_data) is pd.core.frame.DataFrame)
# print(ticker_data.tail())
# if type(ticker_data) is pd.core.frame.DataFrame:
#     data = np.array(ticker_data["Close"].copy().tail(200))
#     reversed_price = data[::-1]
#     # print(reversed_price)
#     print(_af.MMI(reversed_price))
# look_back = 10
# look_back_extra = 11
# print(_sr.getATR(look_back, ticker_data.High[-look_back_extra:-1], ticker_data.Low[-look_back_extra:-1]))