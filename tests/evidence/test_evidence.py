from app.core.evidence.ingest import ingest
from app.core.evidence.validator import validate
from app.core.evidence.hash import fingerprint
def test_evidence():
 e=ingest("TV","GOLD",{"rsi":55},"now",{})
 assert validate(e)
 assert fingerprint(e)
