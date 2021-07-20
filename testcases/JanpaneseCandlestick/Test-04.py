import warnings
warnings.filterwarnings('ignore')

import numpy as np
import os
import sys
METHOD_MODULE_PATH = os.path.abspath('../..')
sys.path.insert(1, METHOD_MODULE_PATH)
import method.algofuncs as _af
import method.JavCan as jModel

BACKTESTING_MODULE_PATH = os.path.abspath('../../backtest')
sys.path.insert(1, BACKTESTING_MODULE_PATH)
from backtesting.backtesting import Backtest, Strategy

path = os.getcwd()


class Test(Strategy):
    def init(self):
        self.buy_price = 0
        self._index = 0

    def next(self):
        if len(self.data.Volume) > 6:
            hasBuySignal = jModel.hasBuySignal(self.data.Open, self.data.Close, self.data.High, self.data.Low, self.data.Body, self.data.Height, self.data.UpShadow, self.data.LowerShadow)
            hasSellSignal = jModel.hasSellSignal(self.data.Open, self.data.Close, self.data.High, self.data.Low, self.data.Body, self.data.Height, self.data.UpShadow, self.data.LowerShadow)

            # if np.datetime64(self.data.Date[-1]) == np.datetime64('2018-06-07T00:00:00.000000000'):
            #     i1 = jModel.isBearishEngulfing(self.data.Open, self.data.Close, self.data.High, self.data.Low, self.data.Body, self.data.Height, self.data.UpShadow, self.data.LowerShadow)
            #     t1 = jModel.isUpTrendV1(self.data.Open, self.data.Close, self.data.High, self.data.Low, self.data.Body, self.data.Height, self.data.UpShadow, self.data.LowerShadow)
            #     p1 = jModel.isWhiteCandlestick(self.data.Open[-2], self.data.Close[-2])
            #     t2 = jModel.isBlackCandlestick(self.data.Open[-1], self.data.Close[-1])
            #     print(i1)
            #     print(t1)
            #     print(p1)
            #     print(t2)
            #     exit()

            # if np.datetime64(self.data.Date[-1]) == np.datetime64('2020-04-01T00:00:00.000000000'):
            #     i1 = jModel.isBullishEngulfing(self.data.Open, self.data.Close, self.data.High, self.data.Low, self.data.Body, self.data.Height, self.data.UpShadow, self.data.LowerShadow)
            #     t1 = jModel.isDownTrendV1(self.data.Open, self.data.Close, self.data.High, self.data.Low, self.data.Body, self.data.Height, self.data.UpShadow, self.data.LowerShadow)
            #     p1 = jModel.isBlackCandlestick(self.data.Open[-2], self.data.Close[-2])
            #     t2 = jModel.isWhiteCandlestick(self.data.Open[-1], self.data.Close[-1])
            #     print(i1)
            #     print(t1)
            #     print(p1)
            #     print(t2)
            #     exit()

            prices = self.data.Close
            if hasBuySignal is True:
                # self.buy()
                self.buy(sl=0.9 * prices[-1])
                # self.buy(sl=0.9 * prices[-1], tp=1.2 * prices[-1])

            if hasSellSignal is True:
                self.position.close()

DATA_PATH = os.path.abspath('../../vn-stock-data/VNX/')
ticker_id = 'BVH'
ticker_data = _af.get_pricing_by_path(DATA_PATH + '/' + ticker_id + '.csv', '2018-01-01')
new_data = jModel.convertToJapanCandle(ticker_data)
bt = Backtest(ticker_data, Test, commission=.005, exclusive_orders=False)
stats = bt.run()
print(stats)
# print(stats['_trades'])
bt.plot()