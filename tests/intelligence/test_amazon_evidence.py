

from app.evidence.evidence_schema import EvidenceContract
def test_amazon_evidence():
 e=EvidenceContract(source="AMAZON",title="Product",content={"asin":"X"})
 assert e.verify_integrity()
