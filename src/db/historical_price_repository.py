from typing import List

from src.db.db import DBConnection
from src.db.models import HistoricalPriceSqlAlchemy
from src.domain.historical_price import HistoricalPrice


class HistoricalPriceRepository:
    def __init__(self, connection: DBConnection):
        self.connection = connection

    def save(self, historical_prices: List[HistoricalPrice]):
        save_session = self.connection.session()
        to_save_list = [HistoricalPriceSqlAlchemy.from_domain(historical_price) for historical_price in
                        historical_prices]
        save_session.bulk_save_objects(to_save_list)
        save_session.commit()
