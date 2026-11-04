from app.trading.gold.strategy.strategy_engine import strategy
def test_adaptive():assert "adaptive" in strategy.run({"prices":[1,2,3]})
