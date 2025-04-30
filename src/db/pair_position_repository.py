from src.db.db import DBConnection
from src.db.models import PairPositionSqlAlchemy
from src.domain.pair_position import PairPosition


class PairPositionRepository:

    def __init__(self, connection: DBConnection):
        self.connection = connection

    def save(self, pair_position: PairPosition):
        self.connection.save(PairPositionSqlAlchemy.from_domain(pair_position))
