# 📈 Pairs Trading Strategy (Statistical Arbitrage)

This project implements a full-featured **cointegration-based pairs trading system** in Python.

It includes:

- Cointegration analysis (ADF test, hedge ratio)
- Historical price loading via `yfinance`
- Z-Score based signal generation
- Live price subscription using **Alpaca API**
- In-memory **PositionManager** for simulation
- Clean architecture with repositories, domain models, and services

---

## 🗂️ Project Structure
```
src/
├── config/             # Env loading, secrets
├── data/               # External APIs (Alpaca, yfinance, scrapers)
├── db/                 # Repositories and SQLAlchemy models
├── domain/             # Core domain models (pure logic)
├── scripts/            # CLI scripts for loading, processing, running
├── services/           # Strategies and managers
├── visualization/      # Optional plots and analytics
└── tests/              # Unit tests
```

---

## 🚀 Getting Started

### 1. Clone the project and install dependencies

```bash
git clone https://github.com/your-username/pairs-trading.git
cd pairs-trading
poetry install
```
### 2. Configure environment variables

Create a .env file in the root directory:

```
ALPACA_API_KEY=your_key
ALPACA_API_SECRET=your_secret
```

## 🧠 Key Concepts
- Cointegration: Detects long-term price relationships between asset pairs
- Z-Score: Measures deviation of spread from its mean to trigger trades
- PairStats: Live metric container (spread, z-score, prices)
- PairPosition: Tracks entry/exit of trades with metadata
- PositionManager: Simulates and tracks open/closed positions

## ⚙️ How to Run

Load SP500 symbols
```
poetry run python src/scripts/load_assets.py
```
Download historical OHLCV data
```
poetry run python src/scripts/load_historical_price.py
```

Calculate cointegration pairs
```
poetry run python src/scripts/calculate_cointegration.py
```

Start live signal tracking
```
poetry run python src/scripts/live_signals.py
```

## 📌 Tech Stack

- Python 3.13+
- poetry for packaging
- yfinance, alpaca-py, SQLAlchemy
- SQLite for local storage

## 📈 Future Enhancements
- Backtesting engine
- Real order execution layer
- Trade analytics & dashboard
- Portfolio-level risk management