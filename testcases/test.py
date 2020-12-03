import os
import pandas as pd
import numpy as np
import method.SaleRules as _sr
import method.algofuncs as _af

a = range(10, 35, 5)
for n in a:
  print(n)

# DATA_PATH = os.path.abspath('../vn-stock-data/VNX/')
# ticker_data = _af.get_pricing_by_path(DATA_PATH + '/' + 'PNJ.csv')
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