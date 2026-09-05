from app.trading.adaptive.state import state
def test_armed():assert state(0,10)=="ARMED"
def test_exit():assert state(-10,10)=="EXIT"
