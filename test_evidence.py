from evidence_engine import EvidenceEngine
def test_v():
    assert EvidenceEngine({'amount':1}).generate_evidence()
