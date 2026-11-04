from app.intelligence.b2b.lead_scoring import LeadScorer
def test_empty_lead_scores_zero():
    assert LeadScorer().score({})["score"] == 0
def test_complete_lead_scores_100():
    lead = {"company_name":"A","website":"https://a.com","email":"a@a.com","country":"PK","industry":"IT","phone":"123"}
    assert LeadScorer().score(lead, mx_valid=True)["score"] == 100
def test_invalid_email_gets_no_email_or_mx_points():
    result = LeadScorer().score({"email":"bad"}, mx_valid=True)
    assert result["breakdown"]["email"]["points"] == 0
    assert result["breakdown"]["mx"]["points"] == 0
def test_mx_points_require_valid_mx():
    result = LeadScorer().score({"email":"a@a.com"})
    assert result["breakdown"]["mx"]["points"] == 0
def test_valid_mx_gets_20_points():
    result = LeadScorer().score({"email":"a@a.com"}, mx_valid=True)
    assert result["breakdown"]["mx"]["points"] == 20
