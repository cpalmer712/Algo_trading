from alpaca.data.live import CryptoDataStream
import csv 
from csv import DictWriter
API_KEY = "PKCI7JHT9DZFWZGMM1YP"
SECRET_KEY = "Qk9FiGkjPJuH0cVk2IMU1haUNM3Hi9kkB1LDe7k8"

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

