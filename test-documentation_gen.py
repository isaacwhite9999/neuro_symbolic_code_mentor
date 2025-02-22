import pytest
from day15_documentation_gen import DocumentationGenerator

def test_extract_functions():
    code = "def foo(): pass"
    gen = DocumentationGenerator(code)
    funcs = gen.extract_functions()
    assert "foo" in funcs
