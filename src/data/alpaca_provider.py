from typing import List, Callable

from alpaca.data.live import StockDataStream


class AlpacaProvider:

    def __init__(self, api_key, api_secret):
        self.data_stream = StockDataStream(api_key, api_secret)

    def add_to_subscribe(self, on_bar: Callable, assets: List[str]) -> None:
        self.data_stream.subscribe_bars(on_bar, *assets)
        print(f"subscribed to {assets}")

    def subscribe(self):
        print("will start listening...")
        self.data_stream.run()
