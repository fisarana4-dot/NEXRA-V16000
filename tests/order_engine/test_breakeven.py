from app.trading.order_engine.breakeven import protect
def test_buy():assert protect("BUY",4400,4410,4390,10)==4400
def test_sell():assert protect("SELL",4400,4390,4410,10)==4400
