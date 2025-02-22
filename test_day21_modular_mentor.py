import pytest
from day21_modular_mentor import ModularCodeMentor

def test_detect_design_patterns():
    code = "# using the singleton pattern here"
    mm = ModularCodeMentor(code)
    found = mm.detect_design_patterns()
    assert "singleton" in found
