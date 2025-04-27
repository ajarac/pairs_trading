from src.config.dotenv import ALPACA_API_KEY, ALPACA_API_SECRET
from src.data.alpaca_provider import AlpacaProvider
from src.db.cointegration_repository import CointegrationRepository
from src.db.db import DBConnection
from src.services.cointegration_strategy import CointegrationStrategy

if __name__ == '__main__':
    connection = DBConnection()

    cointegration_repository = CointegrationRepository(connection)
    alpaca_provider = AlpacaProvider(ALPACA_API_KEY, ALPACA_API_SECRET)
    strategy = CointegrationStrategy(cointegration_repository, alpaca_provider)

    strategy.listen_by_sector()