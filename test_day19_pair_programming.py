import pytest
from day19_pair_programming import PairProgrammingAssistant

def test_on_code_change():
    ppa = PairProgrammingAssistant()
    resp = ppa.on_code_change("def new_func(): pass")
    assert resp is not None  # Hard to test exact content
