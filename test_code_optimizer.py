import pytest
from code_optimizer import CodeOptimizer

def test_optimize_loops():
    code = "for i in range(10): pass"
    opt = CodeOptimizer(code)
    loops = opt.analyze_loops()
    assert loops == 1, "Expected to find exactly 1 loop."
