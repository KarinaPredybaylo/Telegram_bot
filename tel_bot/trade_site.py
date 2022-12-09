import random
import requests
from aiohttp import ClientSession, TCPConnector
from bs4 import BeautifulSoup

TIMEFRAME = ['5m', '15m', '1h', '4h', '1d', '1w', '1M']


def generate_data(pair: str):
    timeframe = random.choice(TIMEFRAME)
    candles = random.randrange(1, 1001)
    ma = random.randrange(2, 5000)
    tp = random.randrange(0, 1000)
    sl = random.randrange(0, 1000)

    return {'pair': pair,
            'timeframe': timeframe,
            'candles': candles,
            'ma': ma,
            'tp': tp,
            'sl': sl}


async def main(text):
    url = 'https://paper-trader.frwd.one/'
    conn = TCPConnector()

    async with ClientSession(connector=conn) as session:
        async with session.post(url, ssl=False, data=generate_data(text)) as response:
            body = await response.text()
            soup = BeautifulSoup(body, 'html.parser')
            try:
                image = soup.find('img')
                image_link = image['src']
                r = requests.get(url + image_link).content
                with open("image.jpg", "wb+") as file:
                    file.write(r)
            except TypeError:
                return 'Error'
