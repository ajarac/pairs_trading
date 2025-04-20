# db/models.py
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Stock(Base):
    __tablename__ = 'Stock'

    symbol = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)
    industry = Column(String)

    def __repr__(self):
        return f"<Stock(symbol='{self.symbol}', name={self.name}, sector={self.sector})>"
