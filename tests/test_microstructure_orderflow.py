import pytest
class V:
    @staticmethod
    def evaluate(s,v): return "BULL" if s>1 and v>1000 else "NEUTRAL"
@pytest.mark.parametrize("s,v,e",[(1.5,1200,"BULL"),(0.5,500,"NEUTRAL")])
def test_vsa(s,v,e): assert V.evaluate(s,v)==e
