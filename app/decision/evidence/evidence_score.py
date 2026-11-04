class EvidenceScore:
    def calculate(self,freshness,reliability,cross_validation,completeness):
        return {"confidence":0.4*freshness+0.3*reliability+0.2*cross_validation+0.1*completeness}
score_engine=EvidenceScore()
