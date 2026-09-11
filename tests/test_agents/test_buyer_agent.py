from app.export_business.buyer_finder.agent import BuyerFinderAgent

def test_country_score():
    assert BuyerFinderAgent().score_buyer({"country":"PK"}) == 20

def test_empty_score():
    assert BuyerFinderAgent().score_buyer({}) == 0

def test_buyer_evidence():
    from app.core.evidence.ingest import ingest
    from app.core.evidence.validator import validate
    e=ingest("BUYER","EXPORT",{"country":"PK"},"now")
    assert validate(e)
    from app.core.evidence.hash import fingerprint
    assert fingerprint(e)

def test_buyer_qualification():
    agent=BuyerFinderAgent()
    assert agent.score_buyer({"country":"PK"}) >= 20

def test_buyer_without_country():
    agent=BuyerFinderAgent()
    assert agent.score_buyer({}) == 0
