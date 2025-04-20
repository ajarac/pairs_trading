# db/setup.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("sqlite:///pairs_trading.db", echo=True)  # echo=True to log SQL queries
SessionLocal = sessionmaker(bind=engine)

# Create the tables
def init_db():
    Base.metadata.create_all(bind=engine)