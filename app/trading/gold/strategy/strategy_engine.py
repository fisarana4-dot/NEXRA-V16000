from app.trading.order_engine.adapter import check,manage
from app.trading.adaptive.context import analyze
from app.trading.gold.core.why_not import explain
from app.trading.gold.core.engine_ids import M15_ENGINE,M1_ENGINE
from app.trading.gold.core.mtf_engine import mtf_engine
from app.trading.gold.signals.signal_engine import signal_decision
from app.trading.gold.structure.structure_engine import structure_engine
from app.trading.gold.core.trade_decision import trade_decision
class GoldStrategy:
    def run(self,d):
        adaptive=analyze(d)
        bias=mtf_engine.bias(d)
        structure=structure_engine.analyze(d)
        blocked=False
        signal=signal_decision(d)
        reason=explain({**d,"blocked":blocked,"signal":signal})
        return {"engine":M15_ENGINE,"reason":reason,"adaptive":adaptive,"bias":bias,"structure":structure,"blocked":blocked,"decision":trade_decision.decide({"blocked":blocked,"signal":signal})}
strategy=GoldStrategy()
