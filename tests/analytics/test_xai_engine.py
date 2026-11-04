def test_xai_engine_module_exists():
    import os
    assert os.path.exists("app/analytics/xai_engine.py")
from app.analytics.xai_engine import XAIEngine
def test_decision(): assert XAIEngine().explain("BUY")["decision"] == "BUY"
def test_confidence(): assert XAIEngine().explain("S",.85)["confidence"] == .85
def test_evidence(): assert XAIEngine().explain("B",evidence={"x":1})["evidence"] == {"x":1}
def test_default_conf(): assert XAIEngine().explain("H")["confidence"] == 0.0
def test_none_evidence(): assert XAIEngine().explain("H",evidence=None)["evidence"] == {}
