# stock_pair.py
from dataclasses import dataclass

import pandas as pd

@dataclass
class StockPair:
    def __init__(self, symbol_x: str, symbol_y: str, prices_x: pd.Series, prices_y: pd.Series):
        self.symbol_x = symbol_x
        self.symbol_y = symbol_y
        self.prices_x = prices_x
        self.prices_y = prices_y

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame({self.symbol_x: self.prices_x, self.symbol_y: self.prices_y})

    def __repr__(self):
        return f"<StockPair {self.symbol_x}/{self.symbol_y}>"