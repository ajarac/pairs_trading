import pandas as pd

def generate_signals(zscore: pd.Series, entry_threshold=2.0, exit_threshold=0.5) -> pd.Series:
    signals = pd.Series(index=zscore.index, dtype="object")

    in_trade = False
    for t in zscore.index:
        z = zscore.loc[t]

        if not in_trade:
            if z > entry_threshold:
                signals[t] = 'short_spread'
                in_trade = True
            elif z < -entry_threshold:
                signals[t] = 'long_spread'
                in_trade = True
        else:
            if abs(z) < exit_threshold:
                signals[t] = 'exit'
                in_trade = False

    return signals