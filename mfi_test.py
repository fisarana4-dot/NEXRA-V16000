import pandas as p
d=p.read_csv('data/silver5y.csv')
from app.trading.gold.flow.mfi_engine import mfi_engine
print(mfi_engine.value(d.High.tolist(),d.Low.tolist(),d.Close.tolist(),d.Volume.tolist()))
