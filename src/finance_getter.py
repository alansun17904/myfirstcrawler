import requests
from bs4 import BeautifulSoup
import re
import os
from pprint import pprint
import logging
import json
import time


class Ticker:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self._soup = self.make_soup(ticker)
        self.name = self.get_ticker_info()
        self.data = {'name': self.name,
                     'ticker': self.ticker,
                     'data': {
                            'close': 0,
                            'change-amount': 0,
                            'change-percent': 0,
                            'date': '',
                            'prev-close': 0,
                            'open': 0,
                            'dayrange': '',
                            '52wrange': '',
                            'pe': 0,
                            'beta': 0,
                            'volume': '',
                            'div-yield': '',
                            'market-cap': 0,
                            'eps': 0
                            }}

    @staticmethod
    def make_soup(ticker: str):
        r = requests.get("https://www.investopedia.com/markets/stocks/" + ticker + '/')  # download inital request
        if r.status_code == 404:  # check status code, for errors and report
            print("Invalid Ticker.")
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            return soup

    def get_ticker_info(self):
        try:
            return self._soup.title.string[:-23].split('-')[1].strip()
        except IndexError:
            print("Invalid ticker name.")
            return ''

    def get_ticker_data(self):
        try:
            self.data['data']['close'] = float(self._soup.find(id='quotePrice').string)
            change_match = re.search(r'(.*)\((.*)%\)$', self._soup.find(id='quoteChange').string)
            self.data['data']['change-amount'] = round(float(change_match.group(1)), 2)
            self.data['data']['change-percent'] = round(float(change_match.group(2)), 2)
            self.data['data']['date'] = self._soup.find(id='quoteDate').string.strip()
            self.data['data']['prev-close'] = round(float(self._soup.find(id='quotePreviousClose').string), 2)
            self.data['data']['open'] = round(float(self._soup.find(id='quoteOpen').string), 2)
            self.data['data']['dayrange'] = self._soup.find(id='quoteDayRange').string.strip()
            self.data['data']['volume'] = int(self._soup.find(id='quoteVolume').string.strip().replace(',', '').split('.')[0])

            # stuff that does not have an id for some reason, search for all tags that don't have attribute id
            # then filters through tags that have the data-type attr, it returns a lot of random stuff but we only
            # want the first 6

            id_filter = lambda t: t.has_attr('class') and t['class'] == ['num'] and not \
                (t.has_attr('id') or t.has_attr('data-type'))

            all_tags = [v.string.strip() for v in self._soup.find_all('td') if id_filter(v)][:6]

            self.data['data']['52wrange'] = all_tags[0]
            self.data['data']['pe'] = float(all_tags[1])
            self.data['data']['beta'] = float(all_tags[2])

            if all_tags[3] == '-':
                self.data['data']['div-yield'] = None
            else:
                self.data['data']['div-yield'] = all_tags[3]

            self.data['data']['market-cap'] = all_tags[4]
            self.data['data']['eps'] = float(all_tags[5])

            return self.data
        except:  # None type errors, any type of connection errors or invalid ticker errors.
            logging.warning("Get Ticker Data Error")
            return


if __name__ == '__main__':
    os.chdir("/data")
    with open("tickers.txt", "r") as f:
        monitored_tickers = f.read().splitlines()
    f.close()

    times = []
    for _ in range(20):
        for tickers in monitored_tickers:
            start = time.time()
            Ticker(tickers).get_ticker_data()
            end = time.time()
            times.append(end-start)
    print(sum(times)/len(times))