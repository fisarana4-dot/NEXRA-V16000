from app.trading.strategy.strategy_engine import strategy_engine
def test_x(): assert strategy_engine.run({"ema_trend":"BUY","rsi_signal":"BUY","vwma_signal":"SELL"})[0]["decision"]=="BUY"
