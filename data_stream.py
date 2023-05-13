from alpaca.data.live import CryptoDataStream
import csv

API_KEY = ""
SECRET_KEY = ""

crypto_stream = CryptoDataStream(API_KEY, SECRET_KEY)


async def bar_callback(bar):

    bar_tuple = bar_to_tuple(bar)
    print(
        bar_tuple
    )

    # open the file in the write mode
    f = open('/Users/kenyattaclark/code/personal/Algo_trading/out.csv', 'a')

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(bar_tuple)

    # close the file
    f.close()


def bar_to_tuple(bar):
    return [bar.symbol, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume, bar.trade_count, bar.vwap]


# Subscribing to bar event
symbol = "BTC/USD"
crypto_stream.subscribe_bars(bar_callback, symbol)

crypto_stream.run()
