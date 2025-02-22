import pytest
from refactor_explainer import explain_refactor_choices

def test_explain_refactor_choices():
    # Minimal check. Possibly mock out LLM to avoid real calls.
    code = "def test_fn(x):\n    if x == None:\n        return True"
    # Call it just to ensure no runtime error
    explain_refactor_choices(code)
    assert True
