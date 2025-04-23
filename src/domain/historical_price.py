import datetime
from dataclasses import dataclass


@dataclass
class HistoricalPrice:
    ticker: str
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

    def __init__(self, ticker: str, date: datetime, open: float, high: float, low: float, close: float, volume: int):
        self.ticker = ticker
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
