from dataclasses import dataclass

import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pandas as pd
from typing import Tuple

from src.domain.candlestick import Candlestick


@dataclass
class Cointegration:
    ticker1: str
    ticker2: str
    cointegrated: bool
    p_value: float
    hedge_ratio: float
    sector: str

    def __init__(self, ticker1: str, ticker2: str, sector: str):
        self.ticker1 = min(ticker1, ticker2)
        self.ticker2 = max(ticker1, ticker2)
        self.cointegrated = False
        self.p_value = 0
        self.sector = sector

    def test_cointegration(self, y: pd.Series, x: pd.Series):
        self.hedge_ratio = self.estimate_hedge_ratio(y, x)
        spread = y - self.hedge_ratio * x
        adf_result = adfuller(spread.dropna())
        self.p_value = adf_result[1]
        self.cointegrated = self.p_value < 0.05

    def calculate_spread(self, candlestick1: Candlestick, candlestick2: Candlestick):
        y = candlestick1.close if candlestick1.ticker == self.ticker1 else candlestick2.close
        x = candlestick2.close if candlestick2.ticker == self.ticker2 else candlestick1.close
        return y - self.hedge_ratio * x

    def get_key(self):
        return f"{self.ticker1}-{self.ticker2}"

    @staticmethod
    def estimate_hedge_ratio(y: pd.Series, x: pd.Series) -> float:
        x_with_const = sm.add_constant(x)
        model = sm.OLS(y, x_with_const).fit()
        return model.params[x.name]
