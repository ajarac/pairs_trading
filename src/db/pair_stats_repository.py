from src.db.db import DBConnection
from src.db.models import PairStatsSqlAlchemy
from src.domain.pair_stats import PairStats


class PairStatsRepository:
    def __init__(self, connection: DBConnection):
        self.connection = connection

    def save(self, pairStats: PairStats):
        self.connection.save(PairStatsSqlAlchemy.from_domain(pairStats))
