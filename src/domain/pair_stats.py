from datetime import datetime

from dataclasses import dataclass


@dataclass
class PairStats:
    ticker1: str
    ticker2: str
    price1: float
    price2: float
    spread: float
    z_score: float
    datetime: datetime

    def __init__(self, ticker1: str, ticker2: str, price1: float, price2: float, spread: float, z_score: float,
                 dt: datetime):
        self.ticker1 = min(ticker1, ticker2)
        self.ticker2 = max(ticker1, ticker2)
        self.price1 = price1
        self.price2 = price2
        self.spread = spread
        self.z_score = z_score
        self.datetime = dt

    def get_key(self):
        return f"{self.ticker1}-{self.ticker2}-{datetime.timestamp(self.datetime)}"

    def get_pair_key(self):
        return f"{self.ticker1}-{self.ticker2}"
