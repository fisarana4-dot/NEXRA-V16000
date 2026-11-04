from ..core.risk_governor import risk_governor
from .sl_guard import sl_ready
def allow(d):
 if d.get("score",0)<7:return False
 if not risk_governor.allow(d):return False
 return sl_ready(d)
