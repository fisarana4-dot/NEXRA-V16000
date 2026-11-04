from app.trading.scout.ai_strategy_scout import AIStrategyScout
def test_short(): assert AIStrategyScout().analyze([1,2])["decision"]=="WAIT"
def test_long(): assert AIStrategyScout().analyze([1,2,3])["decision"]=="LONG"
def test_down(): assert AIStrategyScout().analyze([3,2,1])["decision"]=="SHORT"
def test_mixed(): assert AIStrategyScout().analyze([1,3,2])["decision"]=="WAIT"
