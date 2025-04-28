from enum import Enum


class StrategySignal(Enum):
    LONG_SPREAD = "LONG_SPREAD",
    SHORT_SPREAD = "SHORT_SPREAD",
    CLOSE_SPREAD = "CLOSE_SPREAD"
