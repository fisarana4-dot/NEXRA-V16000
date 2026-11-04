from app.trading.order_engine.contract import Order
def plan(d):
 if d.get("decision")=="NO_TRADE":return None
 return Order(d["decision"],d["price"],d["sl"],d.get("qty",0),d.get("reason",""),d.get("trail",False))
