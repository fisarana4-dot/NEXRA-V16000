from app.core.evidence.validator import validate

class BuyerFinderAgent:
    def __init__(self):
        self.name = "Buyer Agent"

    def score_buyer(self, buyer):
        score = 0
        if buyer.get("country"):
            score += 20
        
        return score


    def qualify_buyer(self,b,e):
        return {"status":"QUALIFIED_FOR_REVIEW"} if validate(e) else {"status":"REJECTED"}
