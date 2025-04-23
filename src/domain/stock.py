from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    name: str
    sector: str
    industry: str

    def __init__(self, symbol: str, name: str, sector: str, industry: str):
        self.symbol = symbol
        self.name = name
        self.sector = sector
        self.industry = industry