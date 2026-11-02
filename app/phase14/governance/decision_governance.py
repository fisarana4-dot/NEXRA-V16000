from dataclasses import dataclass

@dataclass
class DecisionRecord:
    decision_id: str
    approved: bool

class DecisionGovernance:
    def validate(self, decision_id, confidence):
        if not isinstance(decision_id, str) or not decision_id.strip():
            raise ValueError("invalid decision_id")
        if type(confidence) not in (int, float):
            raise ValueError("confidence must be numeric")
        if not 0 <= confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
        return DecisionRecord(decision_id=decision_id, approved=confidence >= 0.8)

    def audit(self, d_id, conf):
        self.validate(d_id, conf)
        return None
