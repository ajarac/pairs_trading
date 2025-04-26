# db/setup.py
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db.models import Base


class DBConnection:
    def __init__(self):
        logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
        self.engine = create_engine("sqlite:///../../pairs_trading.db", echo=False)  # echo=True to log SQL queries
        Base.metadata.create_all(bind=self.engine)

    def session(self):
        maker = sessionmaker(bind=self.engine)
        return maker()
