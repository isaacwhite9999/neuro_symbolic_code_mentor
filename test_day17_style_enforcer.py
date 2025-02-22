import pytest
from day17_style_enforcer import StyleEnforcer

def test_check_style():
    code = "def foo(): # style violation\n    pass"
    se = StyleEnforcer(code)
    v = se.check_style()
    assert len(v) == 1
