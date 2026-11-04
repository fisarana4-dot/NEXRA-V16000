
from app.trading.gold.indicators.rsi_engine import RSIEngine
def test_rsi_bounds():
    r=RSIEngine().value(list(range(1,40))); assert 0<=r<=100
