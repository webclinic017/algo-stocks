import warnings

warnings.filterwarnings('ignore')

import os
import sys

METHOD_MODULE_PATH = os.path.abspath('../..')
sys.path.insert(1, METHOD_MODULE_PATH)
import method.algofuncs as _af
import method.JavCan as jModel

ticker_id = 'GMD'
DATA_PATH = os.path.abspath('../vn-stock-data/VNX/')
ticker_data = _af.get_pricing_by_path(DATA_PATH + '/' + ticker_id + '.csv', '2020-01-01')
# ticker_data.tail(4)



# print(ticker_data)
# print(len(ticker_data.index))
# print(ticker_data[0:5])
# print(ticker_data.size)
# exit()
# last = 0
# np_ticker_data = ticker_data.to_numpy()
# data_len = len(ticker_data.index)
# for i in range(data_len):
#     if i > 2:
#         ii = i + 1
#         data = ticker_data.head(ii)
#         k = data.copy().tail(4)
#         _4daysData = jModel.convertToJapanCandle(k)
#         isHangingMan = jModel.isHangingMan(_4daysData)
#         if isHangingMan is True:
#             print(np_ticker_data[i])
#             last = i
#
# import mplfinance as mpf
# mpf.plot(ticker_data[last-15: last+15],type='candle')
# exit()

# last = ticker_data.tail(1)
# test_data = jModel.convertToJapanCandle(last)
# l_o = test_data['Open'][0]
# l_c = test_data['Close'][0]
# l_h = test_data['Height'][0]
# l_body = test_data['Body'][0]
# l_u = test_data['UpShadow'][0]
# l_bot = test_data['LowerShadow'][0]
#
# print(l_h)
# print(l_bot)
#
# print(f"isWhiteCandlestick: {jModel.isWhiteCandlestick(l_o, l_c)}")
# print(f"isBlackCandlestick: {jModel.isBlackCandlestick(l_o, l_c)}")
# print(f"isSpinningTopCandlestick: {jModel.isSpinningTopCandlestick(l_body, l_h, l_u, l_bot)}")
# print(f"isUmbrellaCandlestick: {jModel.isSpinningTopCandlestick(l_body, l_h, l_u, l_bot)}")
# print(f"isShavenHead: {jModel.isShavenHead(l_h, l_u)}")
# print(f"isShavenBottom: {jModel.isShavenBottom(l_h, l_bot)}")
