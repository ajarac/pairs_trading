from src.db.cointegration_repository import CointegrationRepository
from src.db.historical_price_repository import HistoricalPriceRepository
from src.domain.cointegration import Cointegration
from src.domain.pair_stats import PairStats
from src.domain.zscore_tracker import ZScoreTracker
from src.services.position_manager import PositionManager


class BacktestingService:
    def __init__(self,
                 historical_repo: HistoricalPriceRepository,
                 cointegration_repo: CointegrationRepository,
                 position_manager: PositionManager):
        self.historical_repo = historical_repo
        self.cointegration_repo = cointegration_repo
        self.position_manager = position_manager

    def run(self):
        pairs = self.cointegration_repo.get_top_by_sector()
        for pair in pairs:
            self._backtest_pair(pair)

    def _backtest_pair(self, cointegration: Cointegration):
        df1 = self.historical_repo.get_by_ticker(cointegration.ticker1)
        df2 = self.historical_repo.get_by_ticker(cointegration.ticker2)
        merged = df1.merge(df2, on="date", suffixes=("_1", "_2"))
        zscore_tracker = ZScoreTracker(window_size=100)
        for _, row in merged.iterrows():
            spread = cointegration.calculate_spread_from_prices(row["close_1"], row["close_2"])
            z_score = zscore_tracker.update(spread)
            stats = PairStats(
                ticker1=cointegration.ticker1,
                ticker2=cointegration.ticker2,
                price1=row["close_1"],
                price2=row["close_2"],
                spread=spread,
                z_score=z_score,  # update from a ZScoreTracker
                dt=row["date"]
            )
            self.position_manager.process_signal(stats)
