import pytest
from src.advanced.engine import AdvancedEngine

@pytest.mark.parametrize("value", [0.91, 0.95, 0.99, 1.0])
def test_engine_accepts_values_above_threshold(value):
    assert AdvancedEngine().evaluate(value) is True

@pytest.mark.parametrize("value", [0.0, 0.5, 0.85, 0.9])
def test_engine_rejects_values_at_or_below_threshold(value):
    assert AdvancedEngine().evaluate(value) is False
