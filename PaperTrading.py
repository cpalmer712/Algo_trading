# "Here we would need to know the account position to know if we can make a trade or not.\n",
# "1. We need to know if we can afford to buy. This means do we have enough cash to make a buy\n",
#"2. We need to know how much we need to sell of the current position of the asset that 
# we are interested in. How much do we sell the whole position or a percentage.\n",
  
import pandas as pd
import time
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from my_secrets import APCA_API_KEY_ID, APCA_API_SECRET_KEY

#1
#api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, url)
#balance = api.get_account().cash
#print(f"Paper trading account balance: ${balance}")

#data
df = pd.read_csv('out.csv')
columns = ['Open', 'Close', 'Timestamp']
df.columns = columns
df['Timestamp'] = pd.to_datetime(df['Timestamp'])


trading_client = TradingClient(APCA_API_KEY_ID, APCA_API_SECRET_KEY, paper=True)

#MACD formula
#when MACD is greater than signal, the price goes up
exp1 = df['Close'].ewm(span=12).mean()
exp2 = df['Close'].ewm(span=26).mean() 
macd = exp1 - exp2
signal = macd.ewm(span=9).mean()

def generate_signals(df):
    signals = []
    
    for i in range(1, len(df)):
        if macd.iloc[i] > signal.iloc[i] and macd.iloc[i-1] <= signal.iloc[i-1]:
            order_data_buy = MarketOrderRequest(symbol="BTCUSD", qty=0.1, side=OrderSide.BUY, time_in_force=TimeInForce.GTC)
            trading_client.submit_order(order_data=order_data_buy)
            #signals.append('Buy')   # Buy
        elif macd.iloc[i] < signal.iloc[i] and macd.iloc[i-1] >= signal.iloc[i-1]:
            order_data_sell = MarketOrderRequest(symbol="BTCUSD", qty=0.1, side=OrderSide.SELL, time_in_force=TimeInForce.GTC)
            trading_client.submit_order(order_data=order_data_sell)
            #signals.append('Sell')  # Sell
        else:
            print('Hold')   # Hold

    return signals


while True:
    generate_signals(df)
    time.sleep(60)
