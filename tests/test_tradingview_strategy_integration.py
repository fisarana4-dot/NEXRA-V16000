from app.trading.gold.connectors.tradingview import TV_FIELDS, TradingViewConnector
from app.trading.gold.connectors.tradingview_schema import FIELDS
from app.trading.gold.strategy.strategy_engine import strategy


def test_schema_matches_tradingview_connector_contract():
    assert FIELDS == TV_FIELDS


def test_tradingview_indicator_payload_reaches_buy_decision():
    payload = TradingViewConnector().parse(
        {
            "ema50": 2400,
            "ema200": 2300,
            "rsi": 60,
            "close": 2400,
            "vwma": 2350,
            "volume": 100,
            "swing_high": 2350,
            "swing_low": 2200,
        }
    )

    decision = strategy.run(payload)

    assert decision["decision"] == "BUY"
    assert decision["structure"]["bos"] == "BOS_UP"
    assert decision["structure"]["choch"] == "CHoCH_UP"
