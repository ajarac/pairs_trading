from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str
    name: str
    sector: str
    industry: str

    def __init__(self, symbol: str, name: str, sector: str, industry: str):
        self.ticker = symbol
        self.name = name
        self.sector = sector
        self.industry = industry