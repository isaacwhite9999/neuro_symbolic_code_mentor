# neuro_symbolic_code_mentor/refactor.py

import ast
import astor  # We'll use astor to convert the AST back into source code (pip install astor if needed)

class RefactorTransformer(ast.NodeTransformer):
    """
    An AST transformer that applies symbolic code refactoring rules.
    """

    def visit_Compare(self, node: ast.Compare):
        """
        If we see something like 'x == None', transform into 'x is None'.
        If we see 'x == True', transform into 'x' (or 'not x' for False).
        """
        self.generic_visit(node)

        # We only proceed if there's exactly one comparator
        if len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq):
            comparator = node.comparators[0]
            # Replace '== None' with 'is None'
            if isinstance(comparator, ast.Constant) and comparator.value is None:
                # x == None => x is None
                new_node = ast.Compare(
                    left=node.left,
                    ops=[ast.Is()],
                    comparators=node.comparators
                )
                return ast.copy_location(new_node, node)
            # Replace '== True' with a simpler expression: 'if x:'
            if isinstance(comparator, ast.Constant) and comparator.value is True:
                # x == True => x
                return node.left
            # Replace '== False' => 'not x'
            if isinstance(comparator, ast.Constant) and comparator.value is False:
                # x == False => not x
                new_node = ast.UnaryOp(op=ast.Not(), operand=node.left)
                return ast.copy_location(new_node, node)
        return node

    def visit_For(self, node: ast.For):
        """
        Convert for i in range(len(something)): to direct iteration if possible.
        E.g.: for i in range(len(my_list)): => for item in my_list:
        """
        self.generic_visit(node)

        # Pattern: for i in range(len(...)):
        # node.target => i
        # node.iter => Call(func=Name(id='range'), args=[Call(func=Name(id='len'), args=[...])])
        if (
            isinstance(node.iter, ast.Call) and
            isinstance(node.iter.func, ast.Name) and
            node.iter.func.id == 'range' and
            len(node.iter.args) == 1
        ):
            arg = node.iter.args[0]
            if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name) and arg.func.id == 'len':
                # We found range(len(...))
                sequence = arg.args[0]
                # Create a new loop: for item in sequence:
                # We'll rename 'node.target' to 'item' unless the user wants a specific name
                new_target = ast.Name(id='item', ctx=ast.Store())
                new_for = ast.For(
                    target=new_target,
                    iter=sequence,
                    body=node.body,
                    orelse=node.orelse
                )
                return ast.copy_location(new_for, node)

        return node

def symbolic_refactor(code: str) -> str:
    """
    Applies AST-based symbolic transformations to code and returns the refactored source.
    """
    tree = ast.parse(code)
    transformer = RefactorTransformer()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)
    refactored_code = astor.to_source(new_tree)
    return refactored_code

# Optional: a neural-based improvement for docstrings or function naming
# (Dummy example for demonstration)
def neural_refactor_docstrings(code: str) -> str:
    """
    Calls a neural model to suggest docstring improvements for each function.
    (Implementation depends on your LLM usage; here we'll just do a stub.)
    """
    # Potentially parse the code, find each FunctionDef, add docstrings
    # For now, let's just append a comment to the top to simulate a neural suggestion.
    neural_comment = "# Neural Suggestion: Add docstrings to your functions for clarity.\n"
    return neural_comment + code
