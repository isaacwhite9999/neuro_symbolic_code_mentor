import ast
from llm_handler import LLMAssistant

class UnitTestGenerator:
    """
    Day 9: Scans code for function definitions,
    generates skeleton tests, and adds explanations from LLM.
    """
    def __init__(self, code):
        self.code = code
        self.assistant = LLMAssistant()

    def extract_functions(self):
        """
        Return a list of function names found in the code.
        """
        tree = ast.parse(self.code)
        funcs = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                funcs.append(node.name)
        return funcs

    def generate_test_for_function(self, func_name):
        """
        Produce a minimal test code snippet + LLM-based explanation.
        """
        test_code = f"""
import pytest
# from user_code import {func_name}

def test_{func_name}():
    # Auto-generated test
    result = {func_name}()
    assert result is not None
"""
        prompt = f"Explain a good testing approach for function '{func_name}' in this code:\n{self.code}"
        explanation = self.assistant.generate_explanation(prompt)
        return test_code, explanation

def generate_explainable_tests(code):
    """
    Main Day 9 function: iterates over all functions, prints test stubs + LLM explanations.
    """
    gen = UnitTestGenerator(code)
    funcs = gen.extract_functions()
    if not funcs:
        print("No functions found to generate tests for.")
        return

    for fn in funcs:
        stub, explanation = gen.generate_test_for_function(fn)
        print(f"\n=== Test Stub for '{fn}' ===\n{stub}\nExplanation:\n{explanation}")
