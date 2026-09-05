from app.trading.order_engine.profit_lock import lock
def test_buy():assert lock("BUY",4400,4420,4390,10)==4410
def test_sell():assert lock("SELL",4400,4380,4410,10)==4390
