from app.saas.usage.meter import UsageMeter
def test_meter(): m = UsageMeter(); r = m.track("t1", 100); assert r.tokens_used == 100
