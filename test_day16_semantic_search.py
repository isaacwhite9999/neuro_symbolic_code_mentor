import pytest
from day16_semantic_search import SemanticSearchEngine

def test_build_index():
    code = "class Foo:\n    def bar(self): pass\ndef baz(): pass"
    eng = SemanticSearchEngine(code)
    eng.build_index()
    assert len(eng.index) == 2  # 1 class, 1 function
