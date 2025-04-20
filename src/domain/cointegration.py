import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pandas as pd
from typing import Tuple

def estimate_hedge_ratio(y: pd.Series, x: pd.Series) -> float:
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    return model.params[1]

def test_cointegration(y: pd.Series, x: pd.Series) -> Tuple[bool, float]:
    hedge_ratio = estimate_hedge_ratio(y, x)
    spread = y - hedge_ratio * x
    adf_result = adfuller(spread.dropna())
    p_value = adf_result[1]
    return p_value < 0.05, p_value