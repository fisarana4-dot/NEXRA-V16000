from app.intelligence.investment.valuation_framework import *
def test_metrics():
 assert roe(20,100)==20
 assert abs(growth(120,100)-20)<1e-9
 assert fcf_yield(10,100)==10
 assert debt_ratio(50,100)==.5
 assert pe(5,100)==20
 assert pb(25,100)==4
 assert div_yield(5,100)==5
 assert fair_value(5,20)==100
def test_framework():
 v=ValuationFramework(); assert v.value(5,20)==100
 assert v.metrics({"p":20,"e":100,"oe":80,"m":25,"roe":20,"risk":10})["roe"]==20
