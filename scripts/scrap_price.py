import requests
from bs4 import BeautifulSoup

def scrap_price():
    url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    price_tag = soup.find('fin-streamer', {'data-field': "regularMarketPrice"})
    current_price = float(price_tag.text)
    
    print(f"Current price: {current_price}")
    return current_price