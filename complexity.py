import ast

COMPLEXITY_THRESHOLD = 10

class ComplexityAnalyzer(ast.NodeVisitor):
    """
    Walks the AST, calculates a simple cyclomatic complexity for each function,
    and stores the results in a dict: {function_name: complexity_score}.
    """
    def __init__(self):
        self.current_func = None
        self.complexities = {}  # {func_name: score}

    def visit_FunctionDef(self, node: ast.FunctionDef):
        func_name = node.name
        self.current_func = func_name
        self.complexities[func_name] = 1  # Base complexity
        self.generic_visit(node)  # Continue walking inside the function
        self.current_func = None

    def visit_If(self, node: ast.If):
        if self.current_func:
            self.complexities[self.current_func] += 1
        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        if self.current_func:
            self.complexities[self.current_func] += 1
        self.generic_visit(node)

    def visit_While(self, node: ast.While):
        if self.current_func:
            self.complexities[self.current_func] += 1
        self.generic_visit(node)

    def visit_Try(self, node: ast.Try):
        if self.current_func:
            self.complexities[self.current_func] += 1
        self.generic_visit(node)

    def visit_With(self, node: ast.With):
        if self.current_func:
            self.complexities[self.current_func] += 1
        self.generic_visit(node)

def analyze_complexity(code: str):
    """
    Returns a dict of function_name -> complexity_score.
    """
    tree = ast.parse(code)
    analyzer = ComplexityAnalyzer()
    analyzer.visit(tree)
    return analyzer.complexities

def complexity_report(code: str) -> str:
    """
    Generates a text report highlighting functions above the complexity threshold.
    """
    complexities = analyze_complexity(code)
    if not complexities:
        return "No functions found to analyze."

    report_lines = []
    for func_name, score in complexities.items():
        if score > COMPLEXITY_THRESHOLD:
            report_lines.append(
                f"Function '{func_name}' has COMPLEXITY={score} (threshold={COMPLEXITY_THRESHOLD}) => Consider refactoring!"
            )
        else:
            report_lines.append(
                f"Function '{func_name}' has COMPLEXITY={score}, which is within acceptable range."
            )

    return "\n".join(report_lines)

