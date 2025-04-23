# main.py
from src.data.sp500_scrapper import fetch_sp500_list
from src.db.db import DBConnection
from src.db.stock_repository import StockRepository

if __name__ == '__main__':

    connection = DBConnection()
    stock_repository = StockRepository(connection)
    # Add a trade
    stocks = fetch_sp500_list()

    # Query it back
    for stock in stocks:
        stock_repository.save(stock)
