def detect_swings(values, n=1):
    return [kind for _, kind, _ in detect_swing_points(values, n)]


def detect_swing_points(values, n=1):
    if n < 1:
        raise ValueError("n must be at least 1")

    points = []
    for index in range(n, len(values) - n):
        value = values[index]
        before = values[index - n:index]
        after = values[index + 1:index + n + 1]
        if all(value > other for other in before + after):
            points.append((index, "HIGH", value))
        elif all(value < other for other in before + after):
            points.append((index, "LOW", value))
    return points


def classify_swings(swings):
    highs = [value for kind, value in swings if kind == "HIGH"]
    lows = [value for kind, value in swings if kind == "LOW"]
    structure = []
    if len(highs) > 1:
        structure.append("HH" if highs[1] > highs[0] else "LH")
    if len(lows) > 1:
        structure.append("HL" if lows[1] > lows[0] else "LL")
    return structure


def structure_shift(points, close):
    if not points:
        return None

    highs = [value for _, kind, value in points if kind == "HIGH"]
    lows = [value for _, kind, value in points if kind == "LOW"]
    if highs and close > highs[-1]:
        return "BOS_UP"
    if lows and close < lows[-1]:
        return "BOS_DOWN"
    return None
