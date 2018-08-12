from src.finance_getter import Ticker
from bs4 import BeautifulSoup
import unittest


class TestTicker(unittest.TestCase):
    def setUp(self):
        self.mu = Ticker('MU')
        self.aapl = Ticker('AAPL')
        self.bac = Ticker('BAC')
        self.msft = Ticker('MSFT')

        self.mu.get_ticker_data()
        self.aapl.get_ticker_data()
        self.bac.get_ticker_data()
        self.msft.get_ticker_data()

    def test_create_soup(self):
        self.assertEqual(type(self.mu._soup), BeautifulSoup)
        self.assertEqual(type(self.aapl._soup), BeautifulSoup)
        self.assertEqual(type(self.bac._soup), BeautifulSoup)
        self.assertEqual(type(self.msft._soup), BeautifulSoup)

    def test_get_name(self):
        self.assertEqual(self.mu.name, 'Micron Technology Inc')
        self.assertEqual(self.aapl.name, 'Apple Inc')
        self.assertEqual(self.bac.name, 'Bank of America Corp')
        self.assertEqual(self.msft.name, 'Microsoft Corp')

    def test_get_mu_data(self):
        self.assertEqual(self.mu.data['close'], 51.37)
        self.assertEqual(self.mu.data['change-amount'], -0.89)
        self.assertEqual(self.mu.data['change-percent'], -1.70)
        self.assertEqual(self.mu.data['date'], 'Aug 10, 7:59 PM')
        self.assertEqual(self.mu.data['prev-close'], 52.26)
        self.assertEqual(self.mu.data['open'], 51.25)
        self.assertEqual(self.mu.data['dayrange'], '51.02 - 51.95')
        self.assertEqual(self.mu.data['52wrange'], '28.72 - 64.66')
        self.assertEqual(self.mu.data['pe'], '5.16')
        self.assertEqual(self.mu.data['beta'], 1.799)
        self.assertEqual(self.mu.data['volume'], '31.34M')
        self.assertEqual(self.mu.data['div-yield'], None)
        self.assertEqual(self.mu.data['market-cap'], '63.44B')
        self.assertEqual(self.mu.data['eps'], 9.95)

    def test_get_aapl_data(self):
        self.assertEqual(self.aapl.data['close'], 207.53)
        self.assertEqual(self.aapl.data['change-amount'], -0.62)
        self.assertEqual(self.aapl.data['change-percent'], -0.30)
        self.assertEqual(self.aapl.data['date'], 'Aug 10, 7:59 PM')
        self.assertEqual(self.aapl.data['prev-close'], 208.15)
        self.assertEqual(self.aapl.data['open'], 207.36)
        self.assertEqual(self.aapl.data['dayrange'], '206.67 - 209.10')
        self.assertEqual(self.aapl.data['52wrange'], '149.16 - 209.78')
        self.assertEqual(self.aapl.data['pe'], '18.82')
        self.assertEqual(self.aapl.data['beta'], 1.095)
        self.assertEqual(self.aapl.data['volume'], '24.61M')
        self.assertEqual(self.aapl.data['div-yield'], '2.92/1.41%')
        self.assertEqual(self.aapl.data['market-cap'], '1.02T')
        self.assertEqual(self.aapl.data['eps'], 11.03)

    def test_get_bac_data(self):
        self.assertEqual(self.bac.data['close'], 31.19)
        self.assertEqual(self.bac.data['change-amount'], -0.41)
        self.assertEqual(self.bac.data['change-percent'], -1.30)
        self.assertEqual(self.bac.data['date'], 'Aug 10, 7:59 PM')
        self.assertEqual(self.bac.data['prev-close'], 31.60)
        self.assertEqual(self.bac.data['open'], 31.23)
        self.assertEqual(self.bac.data['dayrange'], '30.90 - 31.33')
        self.assertEqual(self.bac.data['52wrange'], '22.75 - 33.05')
        self.assertEqual(self.bac.data['pe'], '16.07')
        self.assertEqual(self.bac.data['beta'], 1.479)
        self.assertEqual(self.bac.data['volume'], '55.68M')
        self.assertEqual(self.bac.data['div-yield'], '0.48/1.54%')
        self.assertEqual(self.bac.data['market-cap'], '321.55B')
        self.assertEqual(self.bac.data['eps'], 1.94)

    def test_get_msft_data(self):
        self.assertEqual(self.msft.data['close'], 109.00)
        self.assertEqual(self.msft.data['change-amount'], -0.67)
        self.assertEqual(self.msft.data['change-percent'], -0.61)
        self.assertEqual(self.msft.data['date'], 'Aug 10, 7:59 PM')
        self.assertEqual(self.msft.data['prev-close'], 109.67)
        self.assertEqual(self.msft.data['open'], 109.42)
        self.assertEqual(self.msft.data['dayrange'], '108.38 - 109.69')
        self.assertEqual(self.msft.data['52wrange'], '71.70 - 111.15')
        self.assertEqual(self.msft.data['pe'], '51.66')
        self.assertEqual(self.msft.data['beta'], 1.280)
        self.assertEqual(self.msft.data['volume'], '18.18M')
        self.assertEqual(self.msft.data['div-yield'], '1.68/1.54%')
        self.assertEqual(self.msft.data['market-cap'], '847.48B')
        self.assertEqual(self.msft.data['eps'], 2.11)
