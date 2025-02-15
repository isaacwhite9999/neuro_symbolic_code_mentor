from typing import List
from neuro_symbolic_code_mentor.patterns import get_patterns
from neuro_symbolic_code_mentor.neural import NeuralSuggester

class CodeMentor:
    """
    A neuro-symbolic code mentor that analyzes Python code for anti‑patterns
    and returns actionable suggestions.
    """
    
    def __init__(self, use_neural: bool = False):
        self.patterns = get_patterns()
        self.use_neural = use_neural
        if self.use_neural:
            self.neural_suggester = NeuralSuggester()
    
    def analyze(self, code: str) -> List[str]:
        """
        Analyzes the provided code and returns a list of suggestions.
        """
        suggestions = []
        # Symbolic pattern matching
        for pattern, suggestion in self.patterns:
            if pattern.search(code):
                suggestions.append(suggestion)
        # Neural text generation
        if self.use_neural:
            neural_suggestion = self.neural_suggester.generate_suggestions(code)
            suggestions.append(f"Neural Suggestion: {neural_suggestion}")
        return suggestions
