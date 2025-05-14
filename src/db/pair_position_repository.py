from src.db.db import DBConnection
from src.db.models import PairPositionSqlAlchemy
from src.domain.pair_position import PairPosition


class PairPositionRepository:

    def __init__(self, connection: DBConnection):
        self.connection = connection

    def save(self, pair_position: PairPosition):
        domain = PairPositionSqlAlchemy.from_domain(pair_position)
        self.connection.save(domain)

    def update(self, pair_position: PairPosition):
        self.connection.update(PairPositionSqlAlchemy.from_domain(pair_position))