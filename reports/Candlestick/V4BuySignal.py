import warnings

warnings.filterwarnings('ignore')

import os
import sys

METHOD_MODULE_PATH = os.path.abspath('../..')
sys.path.insert(1, METHOD_MODULE_PATH)
import method.JavCan as jModel
import vn_realtime_stock_data.stockRealtimes as stockRealtime
import vn_realtime_stock_data.stockHistory as stockHistory

_upf = lambda c, o, h: ((h - c) if (c > o) else (h - o))
_botf = lambda c, o, l: ((o - l) if (c > o) else (c - l))

data = stockRealtime.getTodayData()
for ticker_data in data:
    ticker = ticker_data['stockSymbol']
    if len(ticker) != 3:
        continue
    _volume = ticker_data['nmTotalTradedQty']
    if type(_volume) is not int or _volume < 500000:
        continue
    _open = ticker_data['openPrice']
    _close = ticker_data['matchedPrice']
    _highest = ticker_data['highest']
    _lowest = ticker_data['lowest']
    _height = _highest - _lowest
    _body = abs(_close - _open)
    _up = _upf(_close, _open, _highest)
    _bot = _botf(_close, _open, _lowest)

    condition = jModel.isWhiteCandlestick(_open, _close)
    # condition = jModel.isHammer(_body, _height, _up, _bot)
    if condition is True:
        # print(ticker)
        history_ticker_data = stockHistory.getStockHistoryData(ticker)
        # print(history_ticker_data)
        # break
        htd = jModel.convertToJapanCandle(history_ticker_data)
        print(history_ticker_data)
        break
        hasBuySignal = jModel.hasCustomBuySignal(htd.Open, htd.Close, htd.High, htd.Low,
                                                 htd.Body, htd.Height, htd.UpShadow,
                                                 htd.LowerShadow, 1)

        print(hasBuySignal)
        break
        # if hasBuySignal is not False:
        #     print(ticker)
        #     break
