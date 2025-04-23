from src.data.history_data_provider import load_history_data
from src.db.db import DBConnection
from src.db.historical_price_repository import HistoricalPriceRepository
from src.db.sector_repository import sectors
from src.db.stock_repository import StockRepository

if __name__ == '__main__':
    connection = DBConnection()
    stock_repository = StockRepository(connection)
    historical_repository = HistoricalPriceRepository(connection)

    for sector in sectors:
        print(f"searching for sector {sector}")
        assets = stock_repository.fetch_by_sector(sector)

        print(f"{len(assets)} assets in sector {sector}")
        for asset in assets:
            print(f"starting loading historical data for {asset}")
            historical_prices = load_history_data(asset.symbol)
            historical_repository.save(historical_prices)
