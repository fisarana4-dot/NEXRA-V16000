from app.trading.gold.volume.rvol_engine import rvol_engine
def test_rvol_above(): assert rvol_engine.analyze([10]*20+[20])["status"]=="ABOVE_AVERAGE"
def test_rvol_below(): assert rvol_engine.analyze([10]*20+[5])["status"]=="BELOW_AVERAGE"
def test_rvol_equal(): assert rvol_engine.analyze([10]*21)["status"]=="AT_AVERAGE"
def test_rvol_insufficient(): assert rvol_engine.analyze([10]*20)["status"]=="INSUFFICIENT_DATA"
def test_rvol_bar_status(): assert rvol_engine.analyze([10]*20+[20])["status"]=="ABOVE_AVERAGE"
