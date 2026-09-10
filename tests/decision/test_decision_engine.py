from app.decision.decision_engine import DecisionEngine
def test_decision_engine():
    result=DecisionEngine().evaluate("GOLD")
    assert result["decision"]=="ANALYZE"
    assert result["input"]=="GOLD"
    assert result["evidence"]["decision"]=="GOLD"
    assert result["evidence"]["confidence"]==27.0
