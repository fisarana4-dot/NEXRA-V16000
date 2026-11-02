from app.phase14.governance.decision_governance import DecisionGovernance; import pytest
def test_governance():
    g = DecisionGovernance(); assert g.audit("d-1", 0.9) is None
    with pytest.raises(ValueError): g.audit("", 0.5)
