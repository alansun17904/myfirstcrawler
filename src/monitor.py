# import asyncio
# import concurrent.futures
import os
from src.finance_getter import Ticker
from time import time
import requests


os.chdir("../data")
print(os.getcwd())
with open("tickers.txt", "r") as f:
    monitored_tickers = f.read().splitlines()
f.close()


async def main(monitored_tickers: list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(monitored_tickers)) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                Ticker,
                symbol)
            for symbol in monitored_tickers
        ]
    for ticker in await asyncio.gather(*futures):
        ticker.get_ticker_data()
        # print(ticker.data)
        # print('-'*80)

print(monitored_tickers)
times = []
for _ in range(20):
    start = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(monitored_tickers))
    end = time()
    times.append(end-start)
print(sum(times)/len(times))
