from src.db.cointegration_repository import CointegrationRepository
from src.db.db import DBConnection
from src.db.historical_price_repository import HistoricalPriceRepository
from src.db.pair_position_repository import PairPositionRepository
from src.services.backtesting_service import BacktestingService
from src.services.position_manager import PositionManager

if __name__ == '__main__':
    connection = DBConnection()

    historical_price_repository = HistoricalPriceRepository(connection)
    cointegration_repository = CointegrationRepository(connection)
    pair_position_repository = PairPositionRepository(connection)
    position_manager = PositionManager(pair_position_repository)

    backtesting_service = BacktestingService(historical_price_repository, cointegration_repository, position_manager)
