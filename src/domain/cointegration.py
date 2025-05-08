from dataclasses import dataclass
from typing import Optional

import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

from src.domain.candlestick import Candlestick


@dataclass
class Cointegration:
    ticker1: str
    ticker2: str
    cointegrated: bool
    p_value: float
    hedge_ratio: float
    sector: str
    regression_y: Optional[str] = None
    regression_x: Optional[str] = None

    def __init__(self, ticker1: str, ticker2: str, sector: str):
        self.ticker1 = min(ticker1, ticker2)
        self.ticker2 = max(ticker1, ticker2)
        self.cointegrated = False
        self.p_value = 0
        self.sector = sector
        self.regression_y = None
        self.regression_x = None

    def test_cointegration(self, y: pd.Series, x: pd.Series):
        self.hedge_ratio = self.estimate_hedge_ratio(y, x)
        self.regression_x = x.name
        self.regression_y = y.name
        spread = y - self.hedge_ratio * x
        adf_result = adfuller(spread.dropna())
        self.p_value = adf_result[1]
        self.cointegrated = self.p_value < 0.05

    def calculate_spread(self, candlestick1: Candlestick, candlestick2: Candlestick):
        price_map = {
            candlestick1.ticker: candlestick1.close,
            candlestick2.ticker: candlestick2.close
        }
        y = price_map[self.regression_y]
        x = price_map[self.regression_x]
        return y - self.hedge_ratio * x


    def calculate_spread_from_prices(self, price1: float, price2: float) -> float:
        price_map = {
            self.ticker1: price1,
            self.ticker2: price2
        }
        y = price_map[self.regression_y]
        x = price_map[self.regression_x]
        return y - self.hedge_ratio * x

    def get_key(self):
        return f"{self.ticker1}-{self.ticker2}"

    @staticmethod
    def estimate_hedge_ratio(y: pd.Series, x: pd.Series) -> float:
        x_with_const = sm.add_constant(x)
        model = sm.OLS(y, x_with_const).fit()
        return model.params[x.name]
