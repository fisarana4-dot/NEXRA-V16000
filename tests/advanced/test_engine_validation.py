import pytest
from src.advanced.engine import AdvancedEngine
def test_default_threshold():
    assert AdvancedEngine().threshold == 0.9
def test_threshold_rejects_bool():
    with pytest.raises(TypeError):
        AdvancedEngine(True)
def test_evaluate_above_threshold():
    assert AdvancedEngine().evaluate(0.95) is True
def test_evaluate_at_threshold():
    assert AdvancedEngine().evaluate(0.9) is False
def test_threshold_rejects_string():
    with pytest.raises(TypeError):
        AdvancedEngine("0.5")
def test_evaluate_rejects_string():
    with pytest.raises(TypeError):
        AdvancedEngine().evaluate("0.5")
def test_evaluate_rejects_bool():
    with pytest.raises(TypeError):
        AdvancedEngine().evaluate(True)
def test_evaluate_rejects_out_of_range():
    with pytest.raises(ValueError):
        AdvancedEngine().evaluate(1.1)
def test_evaluate_rejects_nan():
    with pytest.raises(ValueError):
        AdvancedEngine().evaluate(float("nan"))
def test_evaluate_rejects_infinity():
    with pytest.raises(ValueError):
        AdvancedEngine().evaluate(float("inf"))
def test_evaluate_rejects_negative_infinity():
    with pytest.raises(ValueError):
        AdvancedEngine().evaluate(-float("inf"))
def test_threshold_zero_boundary():
    assert AdvancedEngine(0).threshold == 0
def test_threshold_one_boundary():
    assert AdvancedEngine(1).threshold == 1
def test_threshold_rejects_negative():
    with pytest.raises(ValueError):
        AdvancedEngine(-0.1)


def test_threshold_rejects_nan():
    with pytest.raises(ValueError):
        AdvancedEngine(float("nan"))



def test_threshold_rejects_infinity():
    with pytest.raises(ValueError):
        AdvancedEngine(float("inf"))


def test_threshold_rejects_negative_infinity():
    with pytest.raises(ValueError):
        AdvancedEngine(-float("inf"))


def test_evaluate_at_maximum_boundary():
    assert AdvancedEngine(1).evaluate(1) is False
