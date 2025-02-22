import pytest
from day20_error_pattern import ErrorPatternRecognizer

def test_find_patterns():
    tb = "ZeroDivisionError: division by zero"
    epr = ErrorPatternRecognizer(tb)
    patterns = epr.find_patterns()
    assert any("Check your denominator" in p for p in patterns)
