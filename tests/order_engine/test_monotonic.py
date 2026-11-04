from app.trading.order_engine.trailing import trail
def test_buy():assert trail("BUY",4400,4430,4425,5)>=4425
def test_sell():assert trail("SELL",4400,4370,4375,5)<=4375
