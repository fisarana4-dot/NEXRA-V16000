from app.trading.gold.structure.bos_engine import bos_engine
def test_missing_swings_no_signal(): assert bos_engine.detect({"close":100})==""
from app.trading.gold.structure.choch_engine import choch_engine
def test_downtrend_break_high_is_choch_up(): assert choch_engine.detect({"trend":"DOWN","close":11,"swing_high":10,"swing_low":5})=="CHoCH_UP"
def test_uptrend_break_low_is_choch_down(): assert choch_engine.detect({"trend":"UP","close":4,"swing_high":10,"swing_low":5})=="CHoCH_DOWN"
def test_downtrend_continuation_no_choch(): assert choch_engine.detect({"trend":"DOWN","close":4,"swing_high":10,"swing_low":5})==""
