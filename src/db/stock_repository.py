from typing import List

from src.db.db import DBConnection
from src.db.models import StockSqlAlchemy
from src.domain.stock import Stock


class StockRepository:

    def __init__(self, connection: DBConnection):
        self.connection = connection

    def save(self, stock: Stock):
        save_session = self.connection.session()
        stock_sql_alchemy = StockSqlAlchemy.from_domain(stock)
        save_session.add(stock_sql_alchemy)
        save_session.commit()

    def fetch_by_sector(self, sector: str) -> List[Stock]:
        query_session = self.connection.session()
        stock_sql_alchemy_list = query_session.query(StockSqlAlchemy).where(StockSqlAlchemy.sector == sector)
        return [Stock(s.symbol, s.name, s.sector, s.industry) for s in stock_sql_alchemy_list]
