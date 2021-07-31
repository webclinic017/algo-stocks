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
from backtesting.lib import crossover

from backtesting.test import SMA

path = os.getcwd()


class SmaCross(Strategy):
    def init(self):
        self.orderPending = False
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma3 = self.I(SMA, price, 1)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2) and self.orderPending is False:
            self.buy()
            self.orderPending = True

        if crossover(self.ma2, self.ma1) and self.orderPending is True:
            self.position.close()
            self.orderPending = False

DATA_PATH = os.path.abspath('../../vn-stock-data/VNX/')
ticker_id = 'VRE'
ticker_data = _af.get_pricing_by_path(DATA_PATH + '/' + ticker_id + '.csv', '2018-01-01')
bt = Backtest(ticker_data, SmaCross, commission=.005, exclusive_orders=False)
stats = bt.run()
bt.plot()

