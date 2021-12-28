import warnings

warnings.filterwarnings('ignore')

import os
import sys
import time

METHOD_MODULE_PATH = os.path.abspath('../..')
sys.path.insert(1, METHOD_MODULE_PATH)
import method.JavCan as jModel
import vn_realtime_stock_data.stockRealtimes as stockRealtime
import vn_realtime_stock_data.stockHistory as stockHistory

_upf = lambda c, o, h: ((h - c) if (c > o) else (h - o))
_botf = lambda c, o, l: ((o - l) if (c > o) else (c - l))


data = stockRealtime.getTodayData('hose')
for ticker_data in data:
    ticker = ticker_data['stockSymbol']
    if len(ticker) != 3:
        continue
    _volume = ticker_data['nmTotalTradedQty']
    if type(_volume) is not int or _volume < 2500000:
        continue
    open = ticker_data['openPrice']
    close = ticker_data['matchedPrice']
    highest = ticker_data['highest']
    lowest = ticker_data['lowest']
    total_height = highest - lowest
    body = abs(close - open)
    head = _upf(close, open, highest)
    tail = _botf(close, open, lowest)

    condition1 = True if tail > 0.65 * total_height else False
    condition2 = True if total_height > 0.05 * close else False
    # today has a long tail
    if condition1 is True and condition2 is True:
        history_ticker_data = stockHistory.getStockHistoryData(ticker)  # not include today data
        # # print(history_ticker_data)
        htd = jModel.convertToJapanCandle(history_ticker_data)
        _close = htd.Close.to_numpy()
        isDownTrend = jModel.isDownTrendV2ByRSI(_close)
        if isDownTrend is True:
            print(ticker)