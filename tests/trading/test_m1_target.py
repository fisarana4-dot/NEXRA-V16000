from app.trading.gold.core.m1_target import target
def test_target():assert target({"entry":100,"sl":95,"direction":"BUY","rr":2})==110
def test_sell():assert target({"entry":100,"sl":105,"direction":"SELL","rr":2})==90
