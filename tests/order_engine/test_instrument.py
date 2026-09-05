from app.trading.order_engine.instrument import Instrument
def test_instrument():
 x=Instrument('XAUUSDc',.01,1,.01,100,.01); assert x.volume_step==.01
