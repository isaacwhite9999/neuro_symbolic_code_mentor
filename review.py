# neuro_symbolic_code_mentor/review.py

from typing import List, Dict
from neuro_symbolic_code_mentor.mentor import CodeMentor
from neuro_symbolic_code_mentor.complexity import analyze_complexity, COMPLEXITY_THRESHOLD
from neuro_symbolic_code_mentor.refactor import symbolic_refactor
import difflib

def generate_refactor_diff(original_code: str, refactored_code: str) -> str:
    """
    Produce a unified diff of how the code changed during refactoring,
    which can be displayed in the review.
    """
    original_lines = original_code.splitlines(keepends=True)
    refactored_lines = refactored_code.splitlines(keepends=True)
    diff = difflib.unified_diff(
        original_lines, refactored_lines,
        fromfile="original", tofile="refactored",
        lineterm=""
    )
    return "".join(diff)

def review_code(code: str) -> Dict[str, str]:
    """
    Orchestrates an automated code review across multiple dimensions:
      1. Symbolic pattern checks
      2. Cyclomatic complexity
      3. Potential refactor suggestions

    Returns a dictionary of string sections:
      {
        'patterns': "...",
        'complexity': "...",
        'refactor': "..."
      }
    """

    # -- 1. Symbolic Pattern Checks (Day 1 & 2 logic) --
    mentor = CodeMentor(use_neural=False, use_rl=False)
    suggestions = mentor.analyze(code)  # plain suggestions, no RL
    if suggestions:
        pattern_report = "We identified the following potential issues:\n"
        for idx, suggestion in enumerate(suggestions, 1):
            pattern_report += f"  {idx}. {suggestion}\n"
    else:
        pattern_report = "No pattern-based issues were found."

    # -- 2. Complexity Analysis (Day 4) --
    complexities = analyze_complexity(code)
    if complexities:
        complexity_report = "Function Complexity:\n"
        for func_name, score in complexities.items():
            if score > COMPLEXITY_THRESHOLD:
                complexity_report += (
                    f"  [HIGH]  '{func_name}' => CC={score} (> {COMPLEXITY_THRESHOLD}); "
                    "Consider refactoring into smaller functions.\n"
                )
            else:
                complexity_report += f"  [OK]    '{func_name}' => CC={score}\n"
    else:
        complexity_report = "No functions found, so no complexity data."

    # -- 3. Refactor Suggestions (Day 5) --
    # We'll get a diff showing how 'symbolic_refactor' would transform the code
    refactored = symbolic_refactor(code)
    if refactored.strip() == code.strip():
        refactor_report = "No symbolic refactor changes suggested."
    else:
        diff_text = generate_refactor_diff(code, refactored)
        refactor_report = (
            "Symbolic Refactor Suggestions:\n"
            "Below is a diff of recommended improvements:\n\n"
            + diff_text
        )

    return {
        "patterns": pattern_report,
        "complexity": complexity_report,
        "refactor": refactor_report
    }

def generate_review_report(code: str) -> str:
    """
    Generate a single string that composes all parts of the review into
    a user-friendly message.
    """
    sections = review_code(code)
    # Format them nicely
    report = (
        "=== Automated Code Review ===\n\n"
        "1) Pattern-Based Checks:\n"
        f"{sections['patterns']}\n\n"
        "2) Complexity Analysis:\n"
        f"{sections['complexity']}\n\n"
        "3) Refactoring Suggestions:\n"
        f"{sections['refactor']}\n"
    )
    return report
