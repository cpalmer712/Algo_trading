import csv 
import os
import logging
import logging.config

from my_secrets import API_KEY, SECRET_KEY
from alpaca.data.live import CryptoDataStream

async def bar_callback(bar):
    bar_tuple = [bar.Symbol, bar.Timestamp, bar.Open, bar.High, bar.low, bar.Close, bar.Volume, bar.Trade_count, bar.Vwap]

    logging.debug(bar_tuple)

    f = open(os.path.join(os.getcwd(), 'out.csv'), 'a')
    writer = csv.writer(f)
    writer.writerow(bar_tuple)
    f.close()


# Subscribing to bar event
crypto_stream = CryptoDataStream(API_KEY, SECRET_KEY)
crypto_stream.subscribe_bars(bar_callback, "BTC/USD")
crypto_stream.run()