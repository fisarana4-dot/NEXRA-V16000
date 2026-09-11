from app.export_business.buyer_finder.agent import BuyerFinderAgent

def test_country_score():
    assert BuyerFinderAgent().score_buyer({"country":"PK"}) == 20

def test_empty_score():
    assert BuyerFinderAgent().score_buyer({}) == 0
