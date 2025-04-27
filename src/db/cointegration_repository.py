from sqlalchemy import text

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

    def get_top_by_sector(self):
        query_session = self.connection.session()
        query = text('''WITH ranked_pairs AS (SELECT ticker1,
                                                     ticker2,
                                                     sector,
                                                     value,
                                                     ROW_NUMBER() OVER (PARTITION BY sector ORDER BY value ASC) as rank
                                              FROM cointegration
                                              WHERE cointegrated = 1)
                        SELECT ticker1,
                               ticker2,
                               sector,
                               value
                        FROM ranked_pairs
                        WHERE rank = 1''')
        top_cointegrated = query_session.execute(query).all()
        if top_cointegrated is None:
            return []
        return [Cointegration(ticker1=row.t[0],
                             ticker2=row.t[1],
                             cointegrated=True,
                             value=row.t[3],
                             sector=row.t[2]) for row in top_cointegrated]
