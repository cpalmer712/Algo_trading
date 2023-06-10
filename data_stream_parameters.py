import pandas as pd
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import talib
from backtesting import Strategy
from backtesting.lib import crossover

# Setting parameters for our buy order
market_order_buy = MarketOrderRequest(symbol="BTC/USD", qty=1, side=OrderSide.BUY, time_in_force=TimeInForce.GTC)

# Setting parameters for our buy order
market_order_sell = MarketOrderRequest(symbol="BTC/USD", qty=1, side=OrderSide.SELL, time_in_force=TimeInForce.GTC)


class MACDSTOC(Strategy): 
    
    stoc_buy = False
    stoc_sell = False
    
    def init(self):
      
        #STOCH variables
        self.slowk, self.slowd = self.I(talib.STOCH, self.data.High, self.data.Low, self.data.Close, fastk_period=5, slowk_period=3, slowd_period=3)
        self.macd, self.macdsignal, self.macdhist = self.I(talib.MACD, self.data.Close, fastperiod=12, slowperiod=26, signalperiod=9)
    
    #def barssince(, default=inf):
     #   slowk, slowd = talib.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    
    def next(self):
         
        #if the self.slowd crosses over the self.slowk, the stoc_buy is true and signals a buy
        if crossover(self.slowd, self.slowk):
            self.stoc_buy = True
            self.stoc_sell = False
       #if the slowk crosses over the slowd the stoc_sell is true and signals a sell
        elif crossover(self.slowk, self.slowd):
            self.stoc_sell = True
            self.stoc_buy = False
            
        if self.stoc_sell and crossover(self.macdsignal, self.macd):
            #if this statement is true the below command signals a sell through alpaca api
            market_order_sell()

        elif self.stoc_buy and crossover(self.macd, self.macdsignal):
            #buy command to alpaca api
            market_order_buy()
            
#bt variable runs the backtest dependant on the data, strategy, and cash
#other parameters can be added to more complex strategies. Refer to 
#backtesting.py on github
#bt = Backtest(df, MACDSTOC, cash = 10_000)
data = pd.read_csv('out.csv', header=None)
stats = data(Strategy)
stats