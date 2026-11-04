from app.trading.order_engine.engine import manage
def test_buy():assert manage({"direction":"BUY","entry":4400,"price":4430,"sl":4390,"risk":10,"atr":5})==4425
def test_sell():assert manage({"direction":"SELL","entry":4400,"price":4370,"sl":4410,"risk":10,"atr":5})==4375
