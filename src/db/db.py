# db/setup.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db.models import Base


class DBConnection:
    def __init__(self):
        self.engine = create_engine("sqlite:///../../pairs_trading.db", echo=True)  # echo=True to log SQL queries
        Base.metadata.create_all(bind=self.engine)

    def session(self):
        maker = sessionmaker(bind=self.engine)
        return maker()
