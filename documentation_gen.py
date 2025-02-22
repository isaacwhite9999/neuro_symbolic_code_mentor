import ast
from llm_handler import LLMAssistant

class DocumentationGenerator:
    """
    Day 15: Builds docstrings or external docs for each function, referencing symbolic logic.
    """
    def __init__(self, code):
        self.code = code
        self.assistant = LLMAssistant()

    def extract_functions(self):
        tree = ast.parse(self.code)
        funcs = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                funcs.append(node.name)
        return funcs

    def generate_documentation(self, func_name):
        """
        Calls the LLM to produce a docstring or summary for the function.
        """
        prompt = f"""
Analyze the function '{func_name}' in this code and produce a symbolic summary + usage doc.
Code:
{self.code}
"""
        return self.assistant.generate_explanation(prompt)

def run_documentation_generator(code):
    """
    Main Day 15 function: for each function, produce symbolic doc text.
    """
    generator = DocumentationGenerator(code)
    funcs = generator.extract_functions()
    if not funcs:
        print("No functions found for documentation.")
        return
    print("\n=== Documentation Generator (Day 15) ===\n")
    for fn in funcs:
        doc_text = generator.generate_documentation(fn)
        print(f"\n--- Doc for {fn} ---\n{doc_text}")
