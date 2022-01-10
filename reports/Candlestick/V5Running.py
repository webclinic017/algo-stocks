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

def getMinVolumeByTime():
    from datetime import datetime
    ch = datetime.now().strftime("%H")
    cm = datetime.now().strftime("%M")
    hm = int(ch) + int(cm)/60
    return hm * 100000

def sendTelegramMessage(msg):
    import requests
    telegram_api_url = f"https://api.telegram.org/bot5030570649:AAFbGmcT4T72M_uhiBjy7pEgPi_Lk0j694Y/sendMessage?chat_id=@magnus_vn_algo&text={msg}"
    requests.get(telegram_api_url)
    # if tel_resp.status_code == 200:
    #     print("Notification has been sent on Telegram")
    # else:
    #     print("Could not send Message")


data = stockRealtime.getTodayData('hose')
for ticker_data in data:
    ticker = ticker_data['stockSymbol']
    if len(ticker) != 3:
        continue
    _volume = ticker_data['nmTotalTradedQty']
    _minVol = getMinVolumeByTime()
    if type(_volume) is not int or _volume < _minVol:
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
    if condition1 is True:
        # print(ticker)
        if condition2 is True:
            # print(ticker)
            history_ticker_data = stockHistory.getStockHistoryData(ticker)  # not include today data
            # # print(history_ticker_data)
            htd = jModel.convertToJapanCandle(history_ticker_data)
            _close = htd.Close.to_numpy()
            isDownTrend = jModel.isDownTrendV2ByRSI(_close)
            if isDownTrend is True:
                # print(ticker)
                sendTelegramMessage(ticker)