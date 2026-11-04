from app.trading.gold.strategy.strategy_engine import strategy as gold_strategy
class StrategyEngine:
    def run(self,data): return [gold_strategy.run(data)]
strategy_engine=StrategyEngine()
