from alpaca.data.live import CryptoDataStream

API_KEY = "PKCI7JHT9DZFWZGMM1YP"
SECRET_KEY = "Qk9FiGkjPJuH0cVk2IMU1haUNM3Hi9kkB1LDe7k8"

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
