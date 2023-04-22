from alpaca.data.live import CryptoDataStream

API_KEY = "_ddddddddsafds"
SECRET_KEY = "__"

crypto_stream = CryptoDataStream(API_KEY, SECRET_KEY)

async def bar_callback(bar):
    print(
        bar.close,
    )

# Subscribing to bar event 
symbol = "BTC/USD"
crypto_stream.subscribe_bars(bar_callback, symbol)

data = crypto_stream.run()
data
