import pandas as p
d=p.read_csv('data/silver5y.csv')
from app.trading.gold.flow.obv_divergence import obv_engine
o=obv_engine.value(d.Close.tolist(),d.Volume.tolist())
print(o[-1])
