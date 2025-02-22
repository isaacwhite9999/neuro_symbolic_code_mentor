import pytest
from day14_performance_profiler import PerformanceProfiler

def test_run_profile():
    code = "x = 0\nfor i in range(1000): x += i"
    profiler = PerformanceProfiler(code)
    timing = profiler.run_profile()
    assert "Execution Time:" in timing
