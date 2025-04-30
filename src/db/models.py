from sqlalchemy import Column, String, Date, Float, Integer, Boolean
from sqlalchemy.orm import declarative_base

from src.domain.cointegration import Cointegration
from src.domain.historical_price import HistoricalPrice
from src.domain.pair_stats import PairStats
from src.domain.stock import Stock

Base = declarative_base()


class StockSqlAlchemy(Base):
    __tablename__ = 'Stock'

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String, index=True)
    industry = Column(String)

    @staticmethod
    def from_domain(stock: Stock):
        return StockSqlAlchemy(
            ticker=stock.ticker,
            name=stock.name,
            sector=stock.sector,
            industry=stock.industry
        )

    def __repr__(self):
        return f"<Stock(ticker='{self.ticker}', name={self.name}, sector={self.sector})>"


class HistoricalPriceSqlAlchemy(Base):
    __tablename__ = 'historical_prices'
    __table_args__ = (
        {'sqlite_autoincrement': True}
    )

    ticker = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)

    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)

    @staticmethod
    def from_domain(historical_price: HistoricalPrice):
        return HistoricalPriceSqlAlchemy(
            ticker=historical_price.ticker,
            date=historical_price.date,
            open=historical_price.open,
            high=historical_price.high,
            low=historical_price.low,
            close=historical_price.close,
            volume=historical_price.volume
        )


class CointegrationSqlAlchemy(Base):
    __tablename__ = 'cointegration'

    ticker1 = Column(String, primary_key=True)
    ticker2 = Column(String, primary_key=True)
    cointegrated = Column(Boolean)
    p_value = Column(Float, index=True)
    hedge_ratio = Column(Float)
    sector = Column(String, index=True)

    @staticmethod
    def from_domain(cointegration: Cointegration):
        return CointegrationSqlAlchemy(
            ticker1=cointegration.ticker1,
            ticker2=cointegration.ticker2,
            cointegrated=cointegration.cointegrated,
            p_value=cointegration.p_value,
            hedge_ratio=cointegration.hedge_ratio,
            sector=cointegration.sector
        )


class PairStatsSqlAlchemy(Base):
    __tablename__ = 'pair_stats'

    ticker1 = Column(String, primary_key=True)
    ticker2 = Column(String, primary_key=True)
    spread = Column(Float)
    z_score = Column(Float)
    datetime = Column(Date)

    @staticmethod
    def from_domain(pairStats: PairStats):
        return PairStatsSqlAlchemy(
            ticker1=pairStats.ticker1,
            ticker2=pairStats.ticker2,
            spread=pairStats.spread,
            z_score=pairStats.z_score,
            datetime=pairStats.datetime
        )
