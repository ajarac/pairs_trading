from src.db.cointegration_repository import CointegrationRepository
from src.db.db import DBConnection
from src.db.historical_price_repository import HistoricalPriceRepository
from src.db.sector_repository import sectors
from src.db.stock_repository import StockRepository
from src.services.cointegration_service import CointegrationService

if __name__ == '__main__':
    connection = DBConnection()

    historical_price_repository = HistoricalPriceRepository(connection)
    stock_repository = StockRepository(connection)
    cointegration_repository = CointegrationRepository(connection)

    cointegration_service = CointegrationService(historical_price_repository, stock_repository, cointegration_repository)
    cointegration_service.load_historical_data()
    for sector in sectors:
        print(f"SECTOR {sector}")
        cointegration_service.calculate_by_sector(sector)
