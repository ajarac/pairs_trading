# main.py
from src.data.sp500_scrapper import fetch_sp500_list
from src.db.db import init_db, SessionLocal
from src.db.models import Stock

if __name__ == '__main__':
    init_db()
    session = SessionLocal()

    # Add a trade
    sp500_list = fetch_sp500_list()

    # Query it back
    for company in sp500_list.iterrows():
        symbol = company[1]['symbol']
        name = company[1]['name']
        sector = company[1]['sector']
        industry = company[1]['industry']
        stock = Stock(symbol=symbol, name=name, sector=sector, industry = industry)
        print(f'{stock}')
        session.add(stock)

    session.commit()
