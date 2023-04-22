import requests
from bs4 import BeautifulSoup 

page = requests.get(
    'https://www.autotrader.com/cars-for-sale/all-cars/ford/ranger/bethany-ok-73008?searchRadius=0&isNewSearch=true&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=25&requestId=2281868035'
    )
soup = BeautifulSoup(page.content, 'html.parser')

page_head = soup.head

print(soup)