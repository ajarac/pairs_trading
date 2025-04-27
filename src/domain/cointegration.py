from dataclasses import dataclass

import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pandas as pd
from typing import Tuple


@dataclass
class Cointegration:
    ticker1: str
    ticker2: str
    cointegrated: bool
    value: float
    sector: str

    def __init__(self, ticker1: str, ticker2: str, cointegrated: bool, value: float, sector: str):
        self.ticker1 = ticker1
        self.ticker2 = ticker2
        self.cointegrated = cointegrated
        self.value = value
        self.sector = sector

def estimate_hedge_ratio(y: pd.Series, x: pd.Series) -> float:
    x_with_const = sm.add_constant(x)
    model = sm.OLS(y, x_with_const).fit()
    return model.params[x.name]

def test_cointegration(y: pd.Series, x: pd.Series) -> Tuple[bool, float]:
    hedge_ratio = estimate_hedge_ratio(y, x)
    spread = y - hedge_ratio * x
    adf_result = adfuller(spread.dropna())
    p_value = adf_result[1]
    return p_value < 0.05, p_value
