from app.core.ai_fusion.risk.trading_guard import safe_trail
from app.core.ai_fusion.risk.trading_guard import allow_sl
from app.core.ai_fusion.risk.trading_guard import gate
def approve(manual=False): return gate(manual)
def approve_ai(manual=False): return approve(manual)
def trade_safe(manual,old_sl,new_sl): return approve_ai(manual) and allow_sl(old_sl,new_sl)
def profit_safe(old,entry,profit): return approve_ai(False) and safe_trail(old,entry,profit)
