import pytest
from test_generator import UnitTestGenerator

def test_extract_functions():
    code = "def foo(): pass"
    gen = UnitTestGenerator(code)
    funcs = gen.extract_functions()
    assert "foo" in funcs
