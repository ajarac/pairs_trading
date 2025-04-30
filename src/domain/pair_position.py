from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.domain.direction import Direction


@dataclass
class PairPosition:
    ticker1: str
    ticker2: str
    direction: Direction
    entry_time: datetime
    entry_z_score: float
    entry_price_ticker1: float
    entry_price_ticker2: float

    exit_time: Optional[datetime] = None
    exit_price_ticker1: Optional[float] = None
    exit_price_ticker2: Optional[float] = None
    exit_z_score: Optional[float] = None

    @property
    def pair_key(self):
        return f"{min(self.ticker1, self.ticker2)}-{max(self.ticker1, self.ticker2)}"

    def get_key(self):
        return f"{self.pair_key}-{datetime}-{datetime.timestamp(self.entry_time)}"

    def is_closed(self) -> bool:
        return self.exit_time is not None
