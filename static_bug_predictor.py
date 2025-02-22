import ast
from llm_handler import LLMAssistant

class StaticBugPredictor:
    """
    Day 12: Uses advanced symbolic rules + an LLM to highlight potential bugs
    before runtime.
    """
    def __init__(self, code):
        self.code = code
        self.issues = []
        self.llm = LLMAssistant()

    def analyze(self):
        """
        Perform symbolic checks: e.g., 
        - detect usage of 'eval'
        - detect redefined built-ins
        - detect unreachable code, etc.
        """
        try:
            tree = ast.parse(self.code)
        except SyntaxError as e:
            self.issues.append(f"SyntaxError: {str(e)}")
            return

        # 1. Check for 'eval'
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'eval':
                self.issues.append("Suspicious usage of 'eval' detected.")

        # 2. Check for redefined built-ins
        builtins = {"print", "len", "range"}  # Expand as needed
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in builtins:
                self.issues.append(f"Redefining built-in function '{node.name}' can cause bugs.")

        # More rules can be added here...

    def predict_buggy_sections(self):
        """
        Day 12 twist: pass the flagged issues to the LLM for further commentary or ranking.
        """
        if not self.issues:
            return "No potential bugs found via symbolic analysis."

        prompt = f"""
We found these symbolic code issues in the user's code:
{self.issues}

Please rank them by severity and provide potential solutions.
Code:
{self.code}
"""
        return self.llm.generate_explanation(prompt)

def run_bug_prediction(code):
    predictor = StaticBugPredictor(code)
    predictor.analyze()
    results = predictor.predict_buggy_sections()
    print("\n=== Predicted Buggy Sections ===\n", results)
