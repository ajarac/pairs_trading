from typing import List, Callable

from alpaca.data import Bar
from alpaca.data.live import StockDataStream

from src.domain.candlestick import Candlestick


class AlpacaProvider:

    def __init__(self, api_key, api_secret):
        self.data_stream = StockDataStream(api_key, api_secret)

    def add_to_subscribe(self, on_bar: Callable, assets: List[str]) -> None:
        async def wrap(bar: Bar):
            candlestick = Candlestick(
                ticker=bar.symbol,
                open=bar.open,
                high=bar.high,
                low=bar.low,
                close=bar.close,
                volume=bar.volume,
                timestamp=bar.timestamp
            )
            on_bar(candlestick)

        self.data_stream.subscribe_bars(wrap, *assets)
        print(f"subscribed to {assets}")

    def subscribe(self):
        print("will start listening...")
        self.data_stream.run()
