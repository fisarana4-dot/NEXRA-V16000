# from app.analytics.global.equity import *
import importlib
e = importlib.import_module("app.analytics.global.equity")
def test_invalid_none(): assert not e.valid(None)
def test_invalid_none(): assert not e.valid(None)
def test_invalid_empty(): assert not e.valid("")
def test_ratio(): assert e.ratio(100, 4) == 25
def test_ratio_zero(): assert e.ratio(100, 0) is None
def test_valid_nonempty(): assert e.valid("AAPL")
def test_valuation_positive(): assert e.valuation_ok(2, 5)
def test_valuation_zero(): assert not e.valuation_ok(0, 5)
def test_roe_numeric(): assert e.roe_ok(12.5)
def test_roe_text(): assert not e.roe_ok("12.5")
def test_usable_roe(): assert e.usable(15)
def test_timestamp_valid(): assert e.timestamp_ok(1000)
def test_timestamp_zero(): assert not e.timestamp_ok(0)
def test_numeric_ok(): assert e.numeric_ok(dict(price=1,eps=2,book_value=3,roe=4,pe=5,pb=6))
def test_positive_valuation(): assert e.positive_valuation({"pe":5,"pb":2})
def test_score(): assert e.score({"roe":20,"pe":5,"pb":2}) == 2.0
def test_sourced_valid(): assert e.sourced("Yahoo Finance")
def test_sourced_blank(): assert not e.sourced("  ")
def test_trusted_missing(): assert not e.trusted({})
def test_trusted_no_source(): assert not e.trusted(dict.fromkeys(e.REQUIRED,1))
def test_trusted_complete(): assert e.trusted(dict(ticker="A",country="PK",exchange="PSX",price=10,eps=2,book_value=5,roe=10,pe=5,pb=2,source="PSX"))
