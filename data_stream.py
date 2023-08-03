from alpaca_trade_api.stream import Stream
import csv 
from my_secrets import APCA_API_KEY_ID, APCA_API_SECRET_KEY

async def bar_callback(BTC):
    print(BTC)

    data = {
        'open': BTC.open,
        'close': BTC.close,
        'timestamp': BTC.timestamp
    }

    with open('/Users/carsonpalmer/PythonProjects/Algorithmic Trading/out.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writerow(data)

crypto_stream = Stream(APCA_API_KEY_ID, APCA_API_SECRET_KEY, raw_data=False)

crypto_stream.subscribe_crypto_bars(bar_callback, 'BTCUSD')
crypto_stream.run()
