from app.trading.gold.data.data_loader import data_loader
def test_loader_preserves_text_time_fields(tmp_path):
    path=tmp_path / "candles.csv"
    path.write_text("time,open,high,low,close,volume\n2026-08-10 01:00,1,2,0,1.5,10\n")
    row=data_loader.load(path)[0]
    assert row["time"] == "2026-08-10 01:00"
    assert row["close"] == 1.5
def test_loader_normalizes_tick_volume(tmp_path):
    path=tmp_path / "candles.csv"
    path.write_text("timestamp,open,high,low,close,tick_volume\n1,1,2,0,1.5,10\n")
    row=data_loader.load(path)[0]
    assert row["timestamp"] == "1"
    assert row["volume"] == 10.0
