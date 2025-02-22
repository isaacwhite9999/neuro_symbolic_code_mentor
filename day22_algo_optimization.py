import ast
from llm_handler import LLMAssistant

class AlgorithmOptimizer:
    """
    Day 22: Identifies algorithmic complexity, suggests optimizations (like better sorting or data structures).
    """
    def __init__(self, code):
        self.code = code
        self.llm = LLMAssistant()

    def analyze_algorithms(self):
        # Toy example: detect "bubble sort" pattern or "insertion sort"
        if "for i in range(len(" in self.code and "for j in range(i+1, len(" in self.code:
            return "Possible bubble sort"
        return "No recognized algorithm pattern"

    def propose_optimizations(self, pattern):
        prompt = f"""
Code:
{self.code}

We detected: {pattern}

Suggest a more optimal algorithm (and explain why) using symbolic reasoning.
"""
        return self.llm.generate_explanation(prompt)

def run_algo_optimization(code):
    optimizer = AlgorithmOptimizer(code)
    pattern = optimizer.analyze_algorithms()
    explanation = optimizer.propose_optimizations(pattern)
    print("\n=== Algorithm Optimization (Day 22) ===\n", explanation)
