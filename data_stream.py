from alpaca.data.live import CryptoDataStream
import csv 

API_KEY = "   "
SECRET_KEY = "  "

crypto_stream = CryptoDataStream(API_KEY, SECRET_KEY)

#https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/#
async def bar_callback(bar):
    print(
        bar
    )
    # open the file in the write mode
    f = open('/Users/carsonpalmer/PythonProjects/Algorithmic Trading/out.csv', 'a')

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow([bar])

    # close the file
    f.close()

# Subscribing to bar event 
symbol = "BTC/USD"
crypto_stream.subscribe_bars(bar_callback, symbol)

data = crypto_stream.run()

