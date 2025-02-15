import pytest
from neuro_symbolic_code_mentor.mentor import CodeMentor

@pytest.fixture
def sample_code():
    return """
def process_list(my_list):
    for i in range(len(my_list)):
        if my_list[i] == None:
            print(my_list[i])
    # TODO: Handle empty list scenario
    """

def test_symbolic_analysis(sample_code):
    mentor = CodeMentor()
    suggestions = mentor.analyze(sample_code)
    # Check for known pattern-based suggestions
    assert any("is None" in s for s in suggestions), "Expected suggestion to replace '== None' with 'is None'."
    assert any("print" in s for s in suggestions), "Expected suggestion to avoid print statements."
    assert any("for" in s for s in suggestions), "Expected suggestion for better iteration."
    assert any("TODO" in s for s in suggestions), "Expected reminder to address TODO comments."

def test_neural_integration(sample_code):
    mentor = CodeMentor(use_neural=True)
    suggestions = mentor.analyze(sample_code)
    # Expect additional neural suggestion appended
    neural_suggestions = [s for s in suggestions if s.startswith("Neural Suggestion:")]
    assert neural_suggestions, "Expected a neural suggestion when neural integration is enabled."
