import pytest
from day18_code_summarizer import CodeSummarizer

def test_summarize_structure():
    code = "class Foo:\n    pass\ndef bar(): pass"
    cs = CodeSummarizer(code)
    structure = cs.summarize_structure()
    assert "Function: bar" in structure
    assert "Class: Foo" in structure
