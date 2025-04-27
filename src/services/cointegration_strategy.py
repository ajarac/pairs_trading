from src.data.alpaca_provider import AlpacaProvider
from src.db.cointegration_repository import CointegrationRepository
from src.domain.candlestick import Candlestick
from src.domain.zscore_tracker import ZScoreTracker


class CointegrationStrategy:
    def __init__(self, cointegration_repository: CointegrationRepository, alpaca_provider: AlpacaProvider):
        self.alpaca_provider = alpaca_provider
        self.cointegration_repository = cointegration_repository
        self.last_candlestick = {}
        self.cointegration_pairs = {}
        self.zscore_trackers = {}

    def listen_by_sector(self):
        top_cointegrations = self.cointegration_repository.get_top_by_sector()

        for cointegration in top_cointegrations:
            self.cointegration_pairs[cointegration.ticker1] = cointegration
            self.cointegration_pairs[cointegration.ticker2] = cointegration
            pair_key = self._pair_key(cointegration.ticker1, cointegration.ticker2)
            self.zscore_trackers[pair_key] = ZScoreTracker(window_size=100)
            self.alpaca_provider.add_to_subscribe(self.handle_bar,
                                                  [cointegration.ticker1, cointegration.ticker2])
        self.alpaca_provider.subscribe()

    async def handle_bar(self, candlestick: Candlestick):
        print(f"{candlestick.ticker} - close price: {candlestick.close}")
        self.last_candlestick[candlestick.ticker] = candlestick
        cointegration = self.cointegration_pairs[candlestick.ticker]
        symbol_pair = cointegration.ticker1 if cointegration.ticker2 == candlestick.ticker else cointegration.ticker2
        if symbol_pair not in self.last_candlestick:
            return

        candlestick_pair = self.last_candlestick[symbol_pair]

        spread = cointegration.calculate_spread(candlestick, candlestick_pair)

        pair_key = self._pair_key(cointegration.ticker1, cointegration.ticker2)
        z_tracker = self.zscore_trackers[pair_key]

        z_score = z_tracker.update(spread)

        print(f"Spread: {spread:.5f}, Z-Score: {z_score:.5f}")

    @staticmethod
    def _pair_key(ticker1: str, ticker2: str) -> str:
        return f"{min(ticker1, ticker2)}-{max(ticker1, ticker2)}"

