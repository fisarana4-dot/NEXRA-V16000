from .validator import validate
from .risk_gate import allow
from .averaging import allow as avg
def check(o,risk=1):
 return validate(o) and allow(risk) and avg(o.direction)
from .trailing import trail
def trail_order(d):
 return trail(d["direction"],d["entry"],d["price"],d["sl"],d["atr"])
from .breakeven import protect
from .profit_lock import lock
def manage(d):
 s=protect(d["direction"],d["entry"],d["price"],d["sl"],d["risk"])
 s=lock(d["direction"],d["entry"],d["price"],s,d["risk"])
 return trail(d["direction"],d["entry"],d["price"],s,d["atr"])
