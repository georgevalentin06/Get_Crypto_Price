import requests as rq
import datetime as dt

API_KEY = '9PDTFA5KCZ8G86HM'
API_KEY_NEWS = '0ed3aac0063a45cbb7a7f056b5e9711d'
yesterday = str(dt.datetime.now().date() - dt.timedelta(days=1))

def get_price(crypto_symbol):

    params = {
        'apikey': API_KEY,
        'function': 'DIGITAL_CURRENCY_DAILY',
        'symbol': crypto_symbol,
        'market': 'EUR'
    }

    response = rq.get('https://www.alphavantage.co/query', params=params)
    data = response.json()

    open_price = data['Time Series (Digital Currency Daily)'][yesterday]['1a. open (EUR)'].split(".")[0]
    close_price = data['Time Series (Digital Currency Daily)'][yesterday]['4a. close (EUR)'].split(".")[0]
    highest_price = data['Time Series (Digital Currency Daily)'][yesterday]['2a. high (EUR)'].split(".")[0]

    print(f'Open price: €{open_price}\n'
          f'Close price: €{close_price}\n'
          f'Highest_price: €{highest_price}\n\n')

def get_news(crypto_symbol):

    params = {
        'apikey': API_KEY_NEWS,
        'q': crypto_symbol,
        'language': 'en'
    }

    response = rq.get('https://newsapi.org/v2/everything', params=params)
    data = response.json()
    articles = []

    print('Most relevant crypto news for today:\n')
    for article in data['articles'][:5]:
        print(article['description'])


get_price('btc')
get_news('btc')
