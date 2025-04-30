import datetime

from dataclasses import dataclass


@dataclass
class PairStats:
    ticker1: str
    ticker2: str
    spread: float
    z_score: float
    datetime: datetime

    def __init__(self, ticker1: str, ticker2: str, spread: float, z_score: float, datetime: datetime):
        self.ticker1 = ticker1
        self.ticker2 = ticker2
        self.spread = spread
        self.z_score = z_score
        self.datetime = datetime
