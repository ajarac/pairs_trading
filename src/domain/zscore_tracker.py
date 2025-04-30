class ZScoreTracker:
    def __init__(self, window_size: int = 100):
        self.window_size = window_size
        self.min_required_size = int(window_size * 0.3)
        self.spreads = []

    def update(self, spread: float) -> float:
        """Add a new spread, maintain rolling window, return the current Z-Score."""
        self.spreads.append(spread)

        # Keep only the last window_size spreads
        if len(self.spreads) > self.window_size:
            self.spreads.pop(0)

        if not self.is_ready():  # Require minimum samples
            return 0.0

        mean_spread = sum(self.spreads) / len(self.spreads)
        std_spread = (sum((s - mean_spread) ** 2 for s in self.spreads) / len(self.spreads)) ** 0.5

        if std_spread == 0:
            return 0.0

        z_score = (spread - mean_spread) / std_spread
        return z_score

    def is_ready(self):
        return len(self.spreads) < self.min_required_size