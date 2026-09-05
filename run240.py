import csv,collections
from app.trading.gold.signals.candle_pattern_engine import candle_pattern_engine as e
r=list(csv.DictReader(open('m1_240.csv')));z=[];p={}
for x in r:o={k:float(x[k]) for k in ('open','high','low','close')};z+=e.detect({**o,'prev':p});p={'high':o['high'],'low':o['low']}
print(len(r),collections.Counter(z))
