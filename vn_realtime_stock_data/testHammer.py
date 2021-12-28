import warnings

warnings.filterwarnings('ignore')

import os
import sys
import numpy as np
from datetime import datetime

METHOD_MODULE_PATH = os.path.abspath('../..')
sys.path.insert(1, METHOD_MODULE_PATH)
import method.JavCan as jModel
import vn_realtime_stock_data.stockHistory as stockHistory

ticker = 'HPG'
# print(ticker)
history_ticker_data = stockHistory.getStockHistoryData(ticker)  # not include today data
# print(history_ticker_data)
# exit()
# print(history_ticker_data)
htd = jModel.convertToJapanCandle(history_ticker_data)
print(htd)
# _open = htd.Open.to_numpy()
# _close = htd.Close.to_numpy()
# _highest = htd.High.to_numpy()
# _lowest = htd.Low.to_numpy()
# _height = htd.Height.to_numpy()
# _body = htd.Body.to_numpy()
# _up = htd.UpShadow.to_numpy()
# _bot = htd.LowerShadow.to_numpy()
# _time = htd.Time.to_numpy()
#
# for idx, x in np.ndenumerate(_open):
#   # _iuc = jModel.isHammer(_body[idx], _height[idx], _up[idx], _bot[idx])
#   if _bot[idx] > 0.6 * _height[idx]:
#   # if _iuc is True:
#       print(datetime.fromtimestamp(int(_time[idx])).strftime("%m/%d/%Y, %H:%M:%S"))
#       print(str(_open[idx]) + '-'+ '-' +str(_highest[idx]) + '-' +str(_lowest[idx]) + '-' +str(_close[idx]) + '-' +str(_time[idx]))
#       print('---------------------------------------------------')

for index, row in htd.iterrows():
    # _iuc = jModel.isHammer(row['Body'], row['Height'], row['UpShadow'], row['LowerShadow'])
    # if _iuc is True:
    if row['LowerShadow'] > 0.6 * row['Body']:
      print(datetime.fromtimestamp(row['Time']).strftime("%m/%d/%Y"))