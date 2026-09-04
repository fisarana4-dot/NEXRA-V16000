from app.trading.gold.data.data_loader import data_loader
from app.trading.gold.indicators.rsi_engine import *
r=data_loader.load("data/gold/full/xauusd-m15-bid-2026-01-01-2026-08-08.csv")
print(len(r),rsi_engine.value([x["close"] for x in r]))
