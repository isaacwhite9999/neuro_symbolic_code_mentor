import difflib
import ast
from llm_handler import LLMAssistant

class MergeConflictAnalyzer:
    """
    Symbolically parses code segments from different branches,
    identifies potential conflicts, and uses an LLM to propose merges.
    """
    def __init__(self, branch_a_code, branch_b_code):
        self.branch_a_code = branch_a_code
        self.branch_b_code = branch_b_code
        self.assistant = LLMAssistant()

    def generate_diff(self):
        """
        Produce a unified diff for reference. (Simple text-based, ignoring actual AST merges.)
        """
        a_lines = self.branch_a_code.splitlines(keepends=True)
        b_lines = self.branch_b_code.splitlines(keepends=True)
        diff = difflib.unified_diff(
            a_lines, b_lines,
            fromfile="branch_a", tofile="branch_b",
            lineterm=""
        )
        return "".join(diff)

    def symbolic_analysis(self):
        """
        Example symbolic logic: parse both branches as AST, check for function redefs or changed signatures.
        """
        issues = []
        try:
            a_tree = ast.parse(self.branch_a_code)
            b_tree = ast.parse(self.branch_b_code)

            a_funcs = {node.name for node in ast.walk(a_tree) if isinstance(node, ast.FunctionDef)}
            b_funcs = {node.name for node in ast.walk(b_tree) if isinstance(node, ast.FunctionDef)}

            overlap = a_funcs.intersection(b_funcs)
            if overlap:
                issues.append(f"Both branches modify these functions: {', '.join(overlap)}")
        except SyntaxError as e:
            issues.append(f"Syntax error in one of the branches: {str(e)}")

        return issues

    def propose_merge_resolution(self):
        """
        Combine everything (diff + symbolic issues) into an LLM prompt to suggest a resolution.
        """
        diff_text = self.generate_diff()
        symbolic_issues = self.symbolic_analysis()
        prompt = f"""
We have two branches of Python code that might conflict.
Branch A code:
{self.branch_a_code}

Branch B code:
{self.branch_b_code}

Diff:
{diff_text}

Symbolic issues:
{symbolic_issues}

Provide a merged version and explain the rationale for each conflict resolution step.
"""
        return self.assistant.generate_explanation(prompt)

def interactive_merge_resolution(code_a, code_b):
    """
    Day 11 main function: merges two code segments with LLM + symbolic analysis.
    """
    analyzer = MergeConflictAnalyzer(code_a, code_b)
    resolution = analyzer.propose_merge_resolution()
    print("\n=== Proposed Merge Resolution ===\n")
    print(resolution)
