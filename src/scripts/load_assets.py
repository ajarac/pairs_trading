# main.py
from db.models import Trade
from db.setup import SessionLocal, init_db

init_db()
session = SessionLocal()

# Add a trade
new_trade = Trade(ticker='AAPL', quantity=10, price=180.50)
session.add(new_trade)
session.commit()

# Query it back
for trade in session.query(Trade).all():
    print(trade)