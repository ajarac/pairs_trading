from sqlalchemy import text

from src.db.db import DBConnection
from src.db.models import CointegrationSqlAlchemy
from src.domain.cointegration import Cointegration


class CointegrationRepository:
    def __init__(self, connection: DBConnection):
        self.connection = connection

    def save(self, cointegration: Cointegration):
        self.connection.save(CointegrationSqlAlchemy.from_domain(cointegration))

    def get_top_by_sector(self):
        query_session = self.connection.session()
        query = text('''WITH ranked_pairs AS (SELECT ticker1,
                                                     ticker2,
                                                     sector,
                                                     hedge_ratio,
                                                     p_value,
                                                     regression_x,
                                                     regression_y,
                                                     ROW_NUMBER() OVER (PARTITION BY sector ORDER BY p_value ASC) as rank
                                              FROM cointegration
                                              WHERE cointegrated = 1)
                        SELECT ticker1,
                               ticker2,
                               sector,
                               hedge_ratio,
                               p_value,
                               regression_x,
                               regression_y
                        FROM ranked_pairs
                        WHERE rank = 1''')
        top_cointegrated = query_session.execute(query).all()
        if top_cointegrated is None:
            return []

        cointegration_list = []
        for row in top_cointegrated:
            cointegration = Cointegration(ticker1=row.t[0], ticker2=row.t[1], sector=row.t[2])
            cointegration.hedge_ratio = row[3]
            cointegration.p_value = row[4]
            cointegration.regression_x = row[5]
            cointegration.regression_y = row[6]
            cointegration_list.append(cointegration)

        return cointegration_list
