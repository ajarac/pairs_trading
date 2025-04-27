import datetime


class Candlestick:
    ticker: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    timestamp: datetime

    def __init__(self, ticker: str, open: float, high: float, low: float, close: float, volume: float, timestamp: datetime):
        self.ticker = ticker
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.timestamp = timestamp
