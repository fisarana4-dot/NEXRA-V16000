from .engine_ids import M1_ENGINE
from ..risk.execution_gate import allow
def execute(d):
 if not d.get("m15_approved"):return {"engine":M1_ENGINE,"decision":"NO_TRADE"}
 if not allow(d):return {"engine":M1_ENGINE,"decision":"NO_TRADE"}
 return {"engine":M1_ENGINE,"decision":d.get("decision","NO_TRADE")}
