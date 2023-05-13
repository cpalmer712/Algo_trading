import pandas as pd
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# Setting parameters for our buy order
market_order_buy = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )

# Setting parameters for our buy order
market_order_sell = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=1,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.GTC
                  )

df = pd.read_csv('out.csv')
columns = ['symbol', 'timestamp', 'tzinfo', 'open', 'high', 'low', 'close', 'volume', 'trade count', 'vwap']
df.columns = columns

L14 = df['low'].rolling(14).min()
H14 = df['high'].rolling(14).max()

def trades():
    if L14 > H14:
        return market_order_sell