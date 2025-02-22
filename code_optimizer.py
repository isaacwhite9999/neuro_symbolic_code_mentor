import ast
from llm_handler import LLMAssistant

class CodeOptimizer:
    """
    Day 8: An interactive explorer that checks code for possible performance issues,
    then uses the LLM for optimization suggestions.
    """
    def __init__(self, code):
        self.code = code
        self.assistant = LLMAssistant()

    def analyze_loops(self):
        """
        Simple example: count how many for/while loops exist.
        Real versions might measure time complexity, spot nested loops, etc.
        """
        tree = ast.parse(self.code)
        loop_count = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While)):
                loop_count += 1
        return loop_count

    def suggest_optimizations(self, context):
        """
        Calls the LLM to propose improvements based on the code and context info.
        """
        prompt = f"""
        Code:
        {self.code}

        Observed context: {context}

        Suggest performance optimizations or data structure improvements.
        """
        return self.assistant.generate_explanation(prompt)

def interactive_optimizer(code):
    """
    Main Day 8 function: prints loop analysis, then repeatedly prompts for 'suggest'
    to show optimization tips from the LLM, or 'quit' to exit.
    """
    optimizer = CodeOptimizer(code)
    loops = optimizer.analyze_loops()
    print(f"Detected {loops} loop(s) in your code.\n")

    while True:
        cmd = input("Enter 'suggest' for optimization tips, or 'quit' to exit: ")
        if cmd.lower() == 'quit':
            break
        if cmd.lower() == 'suggest':
            context_info = f"{loops} total loop(s)"
            suggestions = optimizer.suggest_optimizations(context_info)
            print("\n=== Optimization Suggestions ===\n", suggestions)
