from .contract import Order
def validate(o):
 if o.direction not in ("BUY","SELL") or o.qty<=0:return False
 if o.direction=="BUY" and o.sl>=o.entry:return False
 if o.direction=="SELL" and o.sl<=o.entry:return False
 return True
