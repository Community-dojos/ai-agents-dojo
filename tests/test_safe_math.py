import pytest
from common.safe_math import safe_calculate

def test_arithmetic():
    assert safe_calculate("2 + 3 * 4") == 14

def test_reject_names():
    with pytest.raises(ValueError):
        safe_calculate("__import__('os').system('echo bad')")

def test_reject_long_expression():
    with pytest.raises(ValueError):
        safe_calculate("1" * 101)
