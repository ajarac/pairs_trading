from typing import List

import yfinance as yf

from src.domain.historical_price import HistoricalPrice


def load_history_data(asset: str) -> List[HistoricalPrice]:
    data = yf.Ticker(asset).history(period="5y", interval="1d")

    historical_prices = [
        HistoricalPrice(
            ticker=asset,
            date=index,
            open=row['Open'],
            high=row['High'],
            low=row['Low'],
            close=row['Close'],
            volume=int(row['Volume'])
        )
        for index, row in data.iterrows()
    ]
    return historical_prices
