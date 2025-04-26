from src.db.db import DBConnection
from src.db.models import CointegrationSqlAlchemy
from src.domain.cointegration import Cointegration


class CointegrationRepository:
    def __init__(self, connection: DBConnection):
        self.connection = connection

    def save(self, cointegration: Cointegration):
        cointegration_sql_alchemy = CointegrationSqlAlchemy.from_domain(cointegration)
        save_session = self.connection.session()
        save_session.add(cointegration_sql_alchemy)
        save_session.commit()
