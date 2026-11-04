import csv
def run(p):
 d=list(csv.DictReader(open(p)));return len(d)
from app.trading.gold.indicators.indicator_engine import indicators
def load(p): return list(csv.DictReader(open(p)))
def nums(r): return [float(r[x]) for x in ('open','high','low','close','volume')]
def load_h4(p): return list(csv.DictReader(open(p)))
def load_d1(p): return list(csv.DictReader(open(p)))
def bias(m,h,d): return m>0 and h>0 and d>0
def ema(c): from app.trading.gold.indicators.ema_engine import ema_engine;return ema_engine.ema(c,200)
def rsi(c): from app.trading.gold.indicators.rsi_engine import rsi_engine;return rsi_engine.value(c)
def vwma(c,v): from app.trading.gold.indicators.vwma_engine import vwma_engine;return vwma_engine.value(c,v)
def atr(h,l,c): from app.trading.gold.indicators.atr_engine import atr_engine;return atr_engine.value(h,l,c)
def buy(c,v): return c[-1]>ema(c) and rsi(c)>50 and c[-1]>vwma(c,v)
def ema_now(c): return ema(c[:-1])
def signal(c,v): return ema(c) and c[-1]>ema(c) and rsi(c)>50 and c[-1]>vwma(c,v)
