from app.trading.gold.flow.obv_divergence import obv_engine
def test_obv_up():
 assert obv_engine.value([1,2,3],[10,20,30])[-1]==50
