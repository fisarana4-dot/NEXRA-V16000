from app.core.evidence.adapters.base import SourceAdapter
class TradingViewConnector(SourceAdapter):
    def parse(self,p): return {k:p[k] for k in TV_FIELDS if k in p and p[k] is not None}

TV_FIELDS=("rsi","ema50","ema200","vwma","atr","open","high","low","close","volume","rvol","signal","swing_high","swing_low")
