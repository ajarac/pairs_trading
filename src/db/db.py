# db/setup.py
import logging
from typing import List

from sqlalchemy import create_engine, update
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

    def save(self, value: Base):
        save_session = self.session()
        save_session.add(value)
        save_session.commit()

    def bulk_save(self, values: List[Base]):
        save_session = self.session()
        save_session.bulk_save_objects(values)
        save_session.commit()

    def update(self, value: Base):

        update(value)

