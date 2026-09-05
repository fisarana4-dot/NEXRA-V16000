from app.trading.adaptive.context import analyze
def test_trend():assert analyze({"prices":[1,2,3]})["trend"][0]["type"]=="UPTREND"
from app.trading.adaptive.liquidity import sweep
def test_sweep():assert sweep(11,10,5)=="HIGH_SWEEP"
from app.trading.adaptive.evidence import score,direction
def test_evidence():assert score([40,30])==70
def test_direction():assert direction({"BUY":[2],"SELL":[1]})=="BUY"
