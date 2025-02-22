import pytest
from version_control_assistant import MergeConflictAnalyzer

def test_symbolic_analysis_no_conflict():
    branch_a = "def foo(): pass"
    branch_b = "def bar(): pass"
    analyzer = MergeConflictAnalyzer(branch_a, branch_b)
    issues = analyzer.symbolic_analysis()
    assert not issues, "No overlapping function names => no issues"

def test_symbolic_analysis_conflict():
    branch_a = "def foo():\n    return 42\n"
    branch_b = "def foo():\n    return 99\n"
    analyzer = MergeConflictAnalyzer(branch_a, branch_b)
    issues = analyzer.symbolic_analysis()
    assert "foo" in issues[0], "Expected to detect function 'foo' in both branches"
