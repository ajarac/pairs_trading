# db/models.py
from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    quantity = Column(Integer)
    price = Column(Float)

    def __repr__(self):
        return f"<Trade(ticker='{self.ticker}', qty={self.quantity}, price={self.price})>"