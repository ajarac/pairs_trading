from src.config.dotenv import ALPACA_API_KEY, ALPACA_API_SECRET
from src.data.alpaca_provider import AlpacaProvider
from src.db.cointegration_repository import CointegrationRepository
from src.db.db import DBConnection
from src.db.pair_position_repository import PairPositionRepository
from src.db.pair_stats_repository import PairStatsRepository
from src.services.cointegration_strategy import CointegrationStrategy
from src.services.position_manager import PositionManager

if __name__ == '__main__':
    connection = DBConnection()

    cointegration_repository = CointegrationRepository(connection)
    alpaca_provider = AlpacaProvider(ALPACA_API_KEY, ALPACA_API_SECRET)
    pair_stats_repository = PairStatsRepository(connection)
    pair_position_repository = PairPositionRepository(connection)
    position_manager = PositionManager(pair_position_repository)
    strategy = CointegrationStrategy(cointegration_repository, alpaca_provider, pair_stats_repository, position_manager)

    strategy.listen_by_sector()
