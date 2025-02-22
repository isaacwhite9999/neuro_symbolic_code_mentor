import ast
import astor
from llm_handler import LLMAssistant

class RefactorTransformer(ast.NodeTransformer):
    """
    Similar to Day 5's symbolic refactor, but we store details
    about each transformation for day 10's explanation step.
    """
    def __init__(self):
        super().__init__()
        self.changes = []

    def visit_Compare(self, node):
        self.generic_visit(node)
        # Example transformation: x == None => x is None
        if len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq):
            comp = node.comparators[0]
            if isinstance(comp, ast.Constant) and comp.value is None:
                self.changes.append("Replaced '== None' with 'is None'")
                new_node = ast.Compare(
                    left=node.left,
                    ops=[ast.Is()],
                    comparators=node.comparators
                )
                return ast.copy_location(new_node, node)
        return node

def symbolic_refactor_with_tracking(code):
    """
    Applies symbolic transformations and returns (new_code, changes_list).
    """
    tree = ast.parse(code)
    transformer = RefactorTransformer()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)
    new_code = astor.to_source(new_tree)
    return new_code, transformer.changes

class RefactorExplainer:
    def __init__(self):
        self.assistant = LLMAssistant()

    def explain_refactor(self, original_code, refactored_code, changes):
        """
        Use the LLM to produce a narrative explaining the changes from 'changes' list.
        """
        if not changes:
            return "No changes made."

        change_bullet = "\n".join(f"- {c}" for c in changes)
        prompt = f"""
        Original Code:
        {original_code}

        Refactored Code:
        {refactored_code}

        Symbolic changes:
        {change_bullet}

        Explain each change in plain language referencing best Python practices.
        """
        return self.assistant.generate_explanation(prompt)

def explain_refactor_choices(code):
    """
    Main Day 10 function:
    1) Perform symbolic refactor w/ tracking
    2) Use the LLM to explain each change
    """
    new_code, changes = symbolic_refactor_with_tracking(code)
    if not changes:
        print("No symbolic refactoring changes were applied.")
        return

    explainer = RefactorExplainer()
    explanation = explainer.explain_refactor(code, new_code, changes)
    print("\n=== Refactor Explanation ===\n")
    print("Refactored Code:\n", new_code)
    print("\nExplanation:\n", explanation)
