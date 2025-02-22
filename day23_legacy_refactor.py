import ast
import json
from llm_handler import LLMAssistant

class LegacyRefactorTool:
    """
    Day 23: Merges AST-based refactoring with 'historical context' 
    (like commit logs or older function definitions).
    """
    def __init__(self, code, history_data):
        """
        history_data: e.g. a JSON containing previous function versions or commit messages
        """
        self.code = code
        self.history_data = history_data
        self.llm = LLMAssistant()

    def parse_history(self):
        # For example, parse JSON containing older function signatures
        try:
            return json.loads(self.history_data)
        except:
            return {}

    def propose_legacy_refactor(self):
        history_parsed = self.parse_history()
        prompt = f"""
We have legacy code:
{self.code}

History data:
{history_parsed}

Refactor this code while respecting historical constraints or logic, and 
explain each change symbolically.
"""
        return self.llm.generate_explanation(prompt)

def run_legacy_refactor(code, history):
    lrt = LegacyRefactorTool(code, history)
    result = lrt.propose_legacy_refactor()
    print("\n=== Legacy Code Refactoring (Day 23) ===\n", result)
