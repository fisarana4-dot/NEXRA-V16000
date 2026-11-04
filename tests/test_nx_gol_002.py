from app.trading.gold.strategy.strategy_engine import strategy
def test_x(): assert strategy.run({"ema_trend":"BUY","rsi_signal":"BUY","vwma_signal":"SELL"})["decision"]=="BUY"
