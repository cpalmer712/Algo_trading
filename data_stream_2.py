from alpaca_trade_api.stream import Stream
from my_secrets import APCA_API_KEY_ID, APCA_API_SECRET_KEY 

async def print_quote(q):
    print('quote', q)

async def print_trade(t):
    print('trade', t)

def main():
    stream = Stream(APCA_API_KEY_ID, APCA_API_SECRET_KEY, raw_data=True)
    stream.subscribe_crypto_quotes(print_quote, 'BTCUSD')
    #stream.subscribe_crypto_trades(print_trade, 'BTCUSD')

    @stream.on_bar('BTC/USD')
    async def _(bar):
        print('bar', bar)

    stream.run()

if __name__ == "__main__":
    main()