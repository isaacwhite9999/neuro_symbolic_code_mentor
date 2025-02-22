import pytest
from static_bug_predictor import StaticBugPredictor

def test_detect_eval():
    code = "eval('2+2')"
    sbp = StaticBugPredictor(code)
    sbp.analyze()
    assert any("eval" in i for i in sbp.issues)

def test_built_in_redefinition():
    code = "def print(x): pass"
    sbp = StaticBugPredictor(code)
    sbp.analyze()
    assert any("Redefining built-in" in i for i in sbp.issues)
