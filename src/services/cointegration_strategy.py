from src.data.alpaca_provider import AlpacaProvider
from src.db.cointegration_repository import CointegrationRepository


class CointegrationStrategy:
    def __init__(self, cointegration_repository: CointegrationRepository, alpaca_provider: AlpacaProvider):
        self.alpaca_provider = alpaca_provider
        self.cointegration_repository = cointegration_repository

    def listen_by_sector(self):
        top_cointegrations = self.cointegration_repository.get_top_by_sector()

        for cointegration in top_cointegrations:
            self.alpaca_provider.add_to_subscribe(self.handle_bar,
                                                  [cointegration.ticker1, cointegration.ticker2])
        self.alpaca_provider.subscribe()

    async def handle_bar(self, bar):
        print(f"{bar.symbol} - close price: {bar.close}")
