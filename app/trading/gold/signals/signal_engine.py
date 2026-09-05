from ..risk.sl_guard import sl_ready
from ..risk.power_guard import power_safe
from .trade_filter import trade_filter


class GoldSignals:
    def generate(self,d): return [{"signal":d.get("signal","NO_TRADE")}]
    def _comparison(self,d,value_key,baseline):
        try:
            value=float(d[value_key])
            reference=float(d[baseline]) if isinstance(baseline,str) else baseline
        except (KeyError,TypeError,ValueError): return None
        if value>reference:return "BUY"
        if value<reference:return "SELL"
        return None
    def _directions(self,d):
        return (
            d.get("ema_trend") or self._comparison(d,"ema50","ema200"),
            d.get("rsi_signal") or self._comparison(d,"rsi",50),
            d.get("vwma_signal") or self._comparison(d,"close","vwma"),
        )
    def score(self,d): return sum(direction=="BUY" for direction in self._directions(d))
    def sell_score(self,d): return sum(direction=="SELL" for direction in self._directions(d))
signals=GoldSignals()
def signal_decision(d): return "WAIT" if power_safe(d)=="BLOCK" else "WAIT" if trade_filter.evaluate(d)=="WAIT" else "WAIT" if d.get("execute") and not sl_ready(d) else "BUY" if signals.score(d)>signals.sell_score(d) else "SELL" if signals.sell_score(d)>signals.score(d) else "NO_TRADE"
