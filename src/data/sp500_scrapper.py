from typing import List

import pandas as pd

from src.domain.stock import Stock

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

def fetch_sp500_list() -> List[Stock]:
    tables = pd.read_html(WIKI_URL)
    sp500_list = tables[0]
    sp500_list = sp500_list[['Symbol', 'Security', 'GICS Sector', 'GICS Sub-Industry']]
    sp500_list.columns = ['symbol', 'name', 'sector', 'industry']

    stocks = []

    for company in sp500_list.iterrows():
        symbol = company[1]['symbol']
        name = company[1]['name']
        sector = company[1]['sector']
        industry = company[1]['industry']
        stock = Stock(symbol=symbol, name=name, sector=sector, industry = industry)
        print(f'{stock}')
        stocks.append(stock)

    return stocks