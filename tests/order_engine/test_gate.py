from app.trading.order_engine.engine import check
from app.trading.order_engine.contract import Order
def test_no_average():assert not check(Order("BUY",4400,4390,.1),1,"BUY",1)
def test_allow():assert check(Order("BUY",4400,4390,.1),1,"BUY",0)
