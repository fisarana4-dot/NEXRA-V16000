from app.trading.gold.structure.bos_engine import bos_engine
from app.trading.gold.structure.choch_engine import choch_engine
def test_structure_engines_accept_canonical_lowercase_close():
    bullish={"close":11,"swing_high":10,"swing_low":5}
    bearish={"close":4,"swing_high":10,"swing_low":5}
    assert bos_engine.detect(bullish) == "BOS_UP"
    assert bos_engine.detect(bearish) == "BOS_DOWN"
    assert choch_engine.detect(bullish) == "CHoCH_UP"
