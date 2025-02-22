import pytest
from day23_legacy_refactor import LegacyRefactorTool

def test_parse_history():
    code = "def old_func(): pass"
    history = '{"old_func":["v1","v2"]}'
    lrt = LegacyRefactorTool(code, history)
    parsed = lrt.parse_history()
    assert "old_func" in parsed
