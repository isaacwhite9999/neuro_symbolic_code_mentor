
# neuro_symbolic_code_mentor/mentor.py

from typing import List
from neuro_symbolic_code_mentor.patterns import get_patterns
from neuro_symbolic_code_mentor.neural import NeuralSuggester

class CodeMentor:
    """
    A neuro-symbolic code mentor that analyzes Python code for anti-patterns,
    returning actionable suggestions with optional reinforcement learning (RL) adaptation.
    """
    
    def __init__(self, use_neural: bool = False, use_rl: bool = False):
        self.patterns = get_patterns()  # List of (compiled_pattern, suggestion)
        self.use_neural = use_neural
        self.use_rl = use_rl
        
        if self.use_neural:
            self.neural_suggester = NeuralSuggester()
        if self.use_rl:
            from neuro_symbolic_code_mentor.reinforcement import RLAgent
            self.rl_agent = RLAgent(num_patterns=len(self.patterns))
    
    def analyze(self, code: str, return_raw: bool = False) -> List:
        """
        Analyzes the provided code and returns suggestions.
        
        If `return_raw` is True and RL is enabled, returns a list of tuples
        (pattern_index, suggestion) for interactive feedback.
        Otherwise, returns a list of suggestion strings.
        """
        suggestions = []
        for idx, (pattern, suggestion) in enumerate(self.patterns):
            if pattern.search(code):
                suggestions.append((idx, suggestion))
                
        if self.use_rl:
            # Sort suggestions by RL agent weight (highest first)
            suggestions = sorted(suggestions, key=lambda x: self.rl_agent.get_weight(x[0]), reverse=True)
            if not return_raw:
                # Convert tuples to strings with score annotation
                suggestions = [
                    f"{sugg} (score: {self.rl_agent.get_weight(idx):.2f})" 
                    for idx, sugg in suggestions
                ]
        else:
            suggestions = [sugg for idx, sugg in suggestions]
        
        if self.use_neural:
            neural_suggestion = self.neural_suggester.generate_suggestions(code)
            if self.use_rl and return_raw:
                suggestions.append(("neural", neural_suggestion))
            else:
                suggestions.append(f"Neural Suggestion: {neural_suggestion}")
        
        return suggestions

