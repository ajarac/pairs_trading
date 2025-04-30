from typing import List

import pandas as pd
from pandas import DataFrame

from src.db.db import DBConnection
from src.db.models import HistoricalPriceSqlAlchemy
from src.domain.historical_price import HistoricalPrice


class HistoricalPriceRepository:
    def __init__(self, connection: DBConnection):
        self.connection = connection

    def save(self, historical_prices: List[HistoricalPrice]):
        to_save_list = [HistoricalPriceSqlAlchemy.from_domain(historical_price) for historical_price in
                        historical_prices]
        self.connection.bulk_save(to_save_list)

    def get_all(self) -> DataFrame:
        query = '''SELECT * FROM historical_prices;'''
        return pd.read_sql_query(query, con=self.connection.engine)
