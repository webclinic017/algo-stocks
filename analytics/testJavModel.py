import warnings
warnings.filterwarnings('ignore')

import os
import sys

METHOD_MODULE_PATH = os.path.abspath('../..')
sys.path.insert(1, METHOD_MODULE_PATH)
import method.algofuncs as _af
import method.JavCan as jModel

ticker_id = 'BID'
DATA_PATH = os.path.abspath('../vn-stock-data/VNX/')
ticker_data = _af.get_pricing_by_path(DATA_PATH + '/' + ticker_id + '.csv', '2018-01-01')
# ticker_data.tail(4)

# print(ticker_data)
# print(len(ticker_data.index))
# print(ticker_data[0:5])
# print(ticker_data.size)
# exit()
np_df = ticker_data.to_numpy()
data_len = len(ticker_data.index)
for i in range(data_len):
    if i > 2:
        ii = i + 1
        data = ticker_data.head(ii)
        k = data.copy().tail(4)
        _4daysData = jModel.convertToJapanCandle(k)
        isHangingMan = jModel.isHangingMan(_4daysData)
        # print(data)
        # print(k)
        # print(i)
        # print(np_df[i])
        # exit()
        if isHangingMan is True:
            print(np_df[i])


# isHammer = jModel.isHammer(_4daysData)
# print(isHammer)