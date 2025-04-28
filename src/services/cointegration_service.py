from typing import Tuple

import pandas as pd

from src.db.cointegration_repository import CointegrationRepository
from src.db.historical_price_repository import HistoricalPriceRepository
from src.db.stock_repository import StockRepository
from src.domain.cointegration import Cointegration


class CointegrationService:

    def __init__(self,
                 historical_price_repository: HistoricalPriceRepository,
                 stock_repository: StockRepository,
                 cointegration_repository: CointegrationRepository
                 ):
        self.historical_data = None
        self.historical_price_repository = historical_price_repository
        self.stock_repository = stock_repository
        self.cointegration_repository = cointegration_repository

    def load_historical_data(self):
        self.historical_data = self.historical_price_repository.get_all()

    def calculate_by_sector(self, sector: str):
        # 1. Fetch stocks in the sector
        stocks = self.stock_repository.fetch_by_sector(sector)

        if self.historical_data is None:
            raise ValueError("Historical data not loaded. Call load_historical_data() first.")

        # 2. Pivot historical data: index = date, columns = ticker
        historical_prices = self.historical_data.pivot(index="date", columns="ticker", values="close")

        for i in range(len(stocks)):
            stock_1 = stocks[i]
            ticker_1 = stock_1.ticker  # Or .ticker depending on your model

            if ticker_1 not in historical_prices.columns:
                continue

            series_1 = historical_prices[ticker_1]

            for j in range(i + 1, len(stocks)):
                stock_2 = stocks[j]
                ticker_2 = stock_2.ticker

                if ticker_2 not in historical_prices.columns:
                    continue

                series_2 = historical_prices[ticker_2]

                print(f"Calculating cointegration for {stock_1.name} | {stock_2.name}")

                # 3. Align series properly
                series_1_aligned, series_2_aligned = self.align_series(series_1, series_2)

                # 4. Test cointegration
                cointegration = Cointegration(
                    stock_1.ticker,
                    stock_2.ticker,
                    sector
                )
                try:
                    cointegration.test_cointegration(series_1_aligned, series_2_aligned)
                except Exception as e:
                    print(f"Error calculating cointegration for {ticker_1} and {ticker_2}: {e}")
                    continue

                print(f"Calculated {cointegration}")
                self.cointegration_repository.save(cointegration)

    @staticmethod
    def align_series(y: pd.Series, x: pd.Series) -> Tuple[pd.Series, pd.Series]:
        # Align on index (timestamp), keep only matching timestamps
        y_aligned, x_aligned = y.align(x, join="inner")

        # Optional: make sure they are sorted (usually pandas keeps it)
        y_aligned = y_aligned.sort_index()
        x_aligned = x_aligned.sort_index()

        # Drop NaNs if any (after coercion to numeric)
        mask = (~y_aligned.isna()) & (~x_aligned.isna())
        y_clean = y_aligned[mask]
        x_clean = x_aligned[mask]

        return y_clean, x_clean
