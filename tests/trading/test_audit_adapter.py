from app.trading.casebook.contract import CaseRecord
from app.trading.casebook.audit_adapter import to_audit,audit_report
def test_map():
 c=CaseRecord(engine_id="GOLD_M1_EXECUTION",decision="BUY",score=8,entry=100,sl=99,tp=102)
 a=to_audit(c)
 assert a.engine_id==c.engine_id and a.decision=="BUY"
 assert a.score==8 and a.entry==100 and a.sl==99 and a.tp==102
 r=audit_report(c)
 assert r["decision"]=="PASS"
 assert "BUY" in r["evidence"]
 assert "GOLD_M1_EXECUTION" in r["evidence"]
