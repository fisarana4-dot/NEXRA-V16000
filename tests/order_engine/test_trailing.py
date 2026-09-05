from app.trading.order_engine.trailing import trail
def test_buy():assert trail("BUY",4400,4420,4390,5)==4415
def test_sell():assert trail("SELL",4400,4380,4410,5)==4385
