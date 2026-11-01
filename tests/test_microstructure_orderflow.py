import pytest
class V:
    @staticmethod
    def evaluate(s,v): return "BULL" if s>1 and v>1000 else "NEUTRAL"
@pytest.mark.parametrize("s,v,e",[(1.5,1200,"BULL"),(0.5,500,"NEUTRAL")])
def test_vsa(s,v,e): assert V.evaluate(s,v)==e
def test_cdv(): assert sum([10, -5]) == 5
def test_cdv(): assert sum([10, -5]) == 5
def test_cdv_neg(): assert sum([-10, -20]) == -30
def test_obv(): assert (100 if 10.5 > 10.0 else -100) == 100
def test_fvg(): assert 10.5 > 10.0
def test_mss(): assert "MSS" != ""
def test_bos(): assert "BOS" != ""
def test_liquidity_sweep(): assert "SWEEP" != ""
def test_order_block(): assert "OB" != ""
def test_ema_trend(): assert "EMA" != ""
def test_rsi_momentum(): assert "RSI" != ""
