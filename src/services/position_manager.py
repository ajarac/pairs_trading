import datetime
from typing import Dict, List, Literal

from src.db.pair_position_repository import PairPositionRepository
from src.domain.direction import Direction
from src.domain.pair_position import PairPosition
from src.domain.pair_stats import PairStats


class PositionManager:
    def __init__(self, position_repository: PairPositionRepository):
        self.positions: Dict[str, PairPosition] = {}  # active positions by pair_key
        self.position_repository = position_repository

    def process_signal(self, stats: PairStats):
        current_position = self.positions.get(stats.get_key())

        # OPENING
        if current_position is None:
            if stats.z_score > 2:
                self._open(Direction.SHORT_SPREAD, stats)
            elif stats.z_score < -2:
                self._open(Direction.LONG_SPREAD, stats)

        # CLOSING
        elif current_position.direction == Direction.LONG_SPREAD and stats.z_score > 0:
            self._close(current_position, stats)

        elif current_position.direction == Direction.SHORT_SPREAD and stats.z_score < 0:
            self._close(current_position, stats)

    def _open(self, direction: Direction, stats: PairStats):
        position = PairPosition(
            ticker1=stats.ticker1,
            ticker2=stats.ticker2,
            direction=direction,
            entry_time=stats.datetime,
            entry_z_score=stats.z_score,
            entry_price_ticker1=stats.price1,
            entry_price_ticker2=stats.price2
        )
        self.positions[position.pair_key] = position
        print(f"[OPEN] {direction} {position.pair_key} @ {stats.datetime}, z={stats.z_score:.2f}")
        self.position_repository.save(position)

    def _close(self, position: PairPosition, stats: PairStats):
        position.exit_time = stats.datetime
        position.exit_z_score = stats.z_score
        position.exit_price_ticker1 = stats.price1
        position.exit_price_ticker2 = stats.price2
        del self.positions[position.pair_key]

        # Persist to repository
        self.position_repository.save(position)

        print(f"[CLOSE] {position.direction} {position.pair_key} @ {stats.datetime}, z={stats.z_score:.2f}")

    def get_open_positions(self) -> List[PairPosition]:
        return list(self.positions.values())
