import math

class AdvancedEngine:
    def __init__(self, threshold=0.9):
        if isinstance(threshold, bool):
            raise TypeError("invalid threshold")
        if not isinstance(threshold, (int, float)):
            raise TypeError("threshold must be numeric")
        if not math.isfinite(threshold):
            raise ValueError("threshold must be finite")
        if not 0 <= threshold <= 1:
            raise ValueError("threshold out of range")
        self.threshold = threshold

    def evaluate(self, v):
        if isinstance(v, bool):
            raise TypeError("value must be numeric")
        if not isinstance(v, (int, float)):
            raise TypeError("value must be numeric")
        if not math.isfinite(v):
            raise ValueError("value must be finite")
        if not 0 <= v <= 1:
            raise ValueError("value out of range")
        return v > self.threshold
