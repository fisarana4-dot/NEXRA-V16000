from .regime import detect
from .liquidity import map_levels,sweep
from .evidence import score,direction
from app.trading.gold.indicators.trendline_engine import trendline_engine
def analyze(d):
 t=d.get("prices",[])
 tl=trendline_engine.detect(t)
 r=detect(d.get("slope",0),d.get("volume",0),d.get("base",1))
 lv=map_levels(d.get("highs",t),d.get("lows",t))
 return {"regime":r,"trend":tl,"liquidity":lv,"direction":direction(d.get("evidence",{}))}
