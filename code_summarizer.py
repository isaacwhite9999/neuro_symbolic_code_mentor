import ast
from llm_handler import LLMAssistant

class CodeSummarizer:
    """
    Day 18: Summarizes code structure + explains top-level decisions.
    """
    def __init__(self, code):
        self.code = code
        self.assistant = LLMAssistant()

    def summarize_structure(self):
        tree = ast.parse(self.code)
        summary = []
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                summary.append(f"Function: {node.name}")
            elif isinstance(node, ast.ClassDef):
                summary.append(f"Class: {node.name}")
        return summary

    def explain_decisions(self, structure):
        prompt = f"""
Code structure: {structure}
Code:
{self.code}

Explain the key decisions (why these classes/functions might exist, 
and how they interact) in plain language.
"""
        return self.assistant.generate_explanation(prompt)

def run_code_summarizer(code):
    cs = CodeSummarizer(code)
    structure = cs.summarize_structure()
    explanation = cs.explain_decisions(structure)
    print("\n=== Code Summarizer (Day 18) ===\n")
    print("Structure:", structure)
    print("\nExplanation:\n", explanation)
