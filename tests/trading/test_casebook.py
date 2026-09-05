from app.trading.casebook.contract import CaseRecord
def test_case():
 c=CaseRecord(engine_id="GOLD_M15_PRIMARY",decision="NO_TRADE")
 assert c.engine_id=="GOLD_M15_PRIMARY"
 assert c.decision=="NO_TRADE"
import pytest
def test_bad_engine():
 with pytest.raises(ValueError):
  CaseRecord(engine_id="BAD",decision="BUY")
def test_score():
 c=CaseRecord(engine_id="GOLD_M15_PRIMARY",decision="BUY",score=8)
 assert c.score==8
def test_approval():
 c=CaseRecord(engine_id="GOLD_M1_EXECUTION",decision="BUY",m15_approved=True)
 assert c.m15_approved
def test_direction():
 c=CaseRecord(engine_id="GOLD_M1_EXECUTION",decision="BUY",direction="BUY")
 assert c.direction=="BUY"
def test_tp():
 c=CaseRecord(engine_id="GOLD_M1_EXECUTION",decision="BUY",tp=110)
 assert c.tp==110
def test_entry():
 c=CaseRecord(engine_id="GOLD_M1_EXECUTION",decision="BUY",entry=100)
 assert c.entry==100
def test_sl():
 c=CaseRecord(engine_id="GOLD_M1_EXECUTION",decision="BUY",sl=95)
 assert c.sl==95
