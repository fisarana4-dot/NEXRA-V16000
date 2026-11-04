from app.trading.gold.flow.mfi_engine import mfi_engine
def test_mfi_bounds():
 h=list(range(20,60));l=[x-2 for x in h];c=[x-1 for x in h];v=[100]*40
 r=mfi_engine.value(h,l,c,v);assert 0<=r<=100
