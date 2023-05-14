import os
import logging
import csv
import logging.config
import yaml

from alpaca.data.live import CryptoDataStream
from my_secrets import ALPACA_API_KEY, ALPACA_SECRET_KEY

with open('log_config.yaml', 'r') as log_config:
    config = yaml.safe_load(log_config.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


async def bar_callback(bar):
    bar_tuple = [bar.symbol, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume, bar.trade_count,
                 bar.vwap]

    logging.debug(bar_tuple)

    f = open(os.path.join(os.getcwd(), 'out.csv'), 'a')
    writer = csv.writer(f)
    writer.writerow(bar_tuple)
    f.close()


# Subscribing to bar event
crypto_stream = CryptoDataStream(ALPACA_API_KEY, ALPACA_SECRET_KEY)
crypto_stream.subscribe_bars(bar_callback, "BTC/USD")
crypto_stream.run()
