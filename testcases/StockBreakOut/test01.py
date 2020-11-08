import os
import sys

BACKTESTING_MODULE_PATH = os.path.abspath('../../backtest/backtesting/')
sys.path.insert(1, BACKTESTING_MODULE_PATH)
from backtest.backtesting import Backtest, Strategy

import method.Ticker as Ticker
import method.TakeProfit as TakeProfit
import method.CutLoss as CutLoss
from method.data import get_pricing_by_path
path = os.getcwd()


class StockBreakOut(Strategy):
    def init(self):
        self.buy_price = 0
        self._index = 0
    def next(self):
        prices = self.data.Close
        if len(self.data.Volume) > 66:
            last_price = prices[-1]
            if self.buy_price == 0 and Ticker.isStockOut(prices):
                self.buy_price = last_price
                self.buy()
            if self.buy_price != 0 and (TakeProfit.takeProfit(5, last_price, self.buy_price) or CutLoss.shouldCutLossByPercent(8, last_price, self.buy_price)):
                self.position.close()
                self.buy_price = 0

vn30_ticker = Ticker.getListBlueChips2020()
DATA_PATH = os.path.abspath('../../vn-stock-data/VNX/')
for ticker in vn30_ticker:
    ticker_data = get_pricing_by_path(DATA_PATH+ticker+'.csv')
    bt = Backtest(ticker_data, StockBreakOut, commission=.005, exclusive_orders=False)
    stats = bt.run()
    # bt.plot()
    # print(stats)
    print(ticker)
    print(stats['Sharpe Ratio'])

