from datetime import datetime,timedelta
from app.trading.gold.risk.news_guard import news_protected
def test_news_window():
    t=datetime(2026,8,28,19,0)
    assert news_protected(t-timedelta(minutes=30),t)
    assert news_protected(t,t)
    assert news_protected(t+timedelta(minutes=30),t)
    assert not news_protected(t-timedelta(minutes=31),t)
    assert not news_protected(t+timedelta(minutes=31),t)
