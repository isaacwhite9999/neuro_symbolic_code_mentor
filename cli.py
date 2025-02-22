import sys
import argparse
from dotenv import load_dotenv

# Day 1–2: Mentor (Pattern Matching, RL)
from mentor import CodeMentor

# Day 3: Debugger
from debugger import Debugger

# Day 4: Complexity
from complexity import complexity_report

# Day 5: Refactor
from refactor import symbolic_refactor

# Day 6: Automated Review
from review import review_code

# Day 7: Interactive Code Discussion
from discussion import interactive_code_discussion

# Day 8: Code Optimizer
from code_optimizer import interactive_optimizer

# Day 9: Explainable Test Generator
from test_generator import generate_explainable_tests

# Day 10: Refactor Explainer
from refactor_explainer import explain_refactor_choices

# Day 11: Version Control Assistant (Merge)
from version_control_assistant import interactive_merge_resolution

# Day 12: Static Bug Predictor
from static_bug_predictor import run_bug_prediction

# Day 13: Security Analyzer
from security_analyzer import run_security_analysis


def get_code_input():
    """
    Allows multi-line code input until user types 'END' on a new line.
    """
    print("Paste your Python code (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    return '\n'.join(lines)


def main():
    load_dotenv()  # Load environment variables (OPENAI_API_KEY, etc.)

    parser = argparse.ArgumentParser(description="Neuro-Symbolic Code Mentor (Days 1–13)")

    # ========== Existing Days 1–6 Flags ==========

    # (Optional) If you want a single "mentor" mode for day 1–2:
    parser.add_argument("--mentor", action="store_true",
                        help="Analyze code with pattern matching + optional RL (Days 1–2).")
    parser.add_argument("--rl", action="store_true", help="Enable RL feedback (Day 2).")
    parser.add_argument("--neural", action="store_true", help="Enable neural suggestions (Day 1).")

    # Day 3:
    parser.add_argument("--debug", action="store_true", help="Run symbolic debugging (Day 3).")
    parser.add_argument("--interactive-debug", action="store_true",
                        help="Symbolic debugger with post-mortem debugging (Day 3, optional).")

    # Day 4:
    parser.add_argument("--complexity", action="store_true", help="Analyze cyclomatic complexity (Day 4).")

    # Day 5:
    parser.add_argument("--refactor", action="store_true", help="Apply symbolic refactor (Day 5).")

    # Day 6:
    parser.add_argument("--review", action="store_true", help="Run automated code review (Day 6).")

    # ========== New Days 7–10 Flags ==========

    # Day 7
    parser.add_argument("--discussion", action="store_true",
                        help="Interactive code discussion with LLM + symbolic analysis (Day 7).")
    # Day 8
    parser.add_argument("--optimize", action="store_true",
                        help="Interactive code optimization explorer (Day 8).")
    # Day 9
    parser.add_argument("--testgen", action="store_true",
                        help="Generate explainable unit tests (Day 9).")
    # Day 10
    parser.add_argument("--refactor-explain", action="store_true",
                        help="Explain symbolic refactor changes (Day 10).")

    # ========== Days 11–13 Flags ==========

    # Day 11
    parser.add_argument("--merge-vcs", action="store_true",
                        help="Version control assistant for merge resolutions (Day 11).")

    # Day 12
    parser.add_argument("--predict-bugs", action="store_true",
                        help="Static analysis + symbolic rules to predict potential bugs (Day 12).")

    # Day 13
    parser.add_argument("--security-check", action="store_true",
                        help="Analyze code security vulnerabilities symbolically (Day 13).")

    args = parser.parse_args()

    # If using a multi-step input (like Day 11 merges), handle separately:
    if args.merge_vcs:
        print("Paste code for branch A (END to finish):")
        branch_a = get_code_input()
        print("Paste code for branch B (END to finish):")
        branch_b = get_code_input()
        interactive_merge_resolution(branch_a, branch_b)
        sys.exit(0)

    # For everything else, we'll just read a single code snippet from user:
    code = get_code_input()

    # ========== Day 3: Debugging (Note: interactive_debug is currently a placeholder in your debugger code) ==========
    if args.debug or args.interactive_debug:
        dbg = Debugger(code)
        result = dbg.debug_code()
        print("\n=== Debugger Output ===\n", result)
        sys.exit(0)

    # ========== Day 4: Complexity ==========
    if args.complexity:
        print("\n=== Complexity Analysis ===\n")
        report = complexity_report(code)
        print(report)
        sys.exit(0)

    # ========== Day 5: Refactor ==========
    if args.refactor:
        print("\n=== Symbolic Refactoring ===")
        new_code = symbolic_refactor(code)
        print("\nRefactored Code:\n", new_code)
        sys.exit(0)

    # ========== Day 6: Review ==========
    if args.review:
        print("\n=== Automated Code Review ===")
        review_result = review_code(code)
        print(review_result)
        sys.exit(0)

    # ========== Day 7: Discussion ==========
    if args.discussion:
        interactive_code_discussion(code)
        sys.exit(0)

    # ========== Day 8: Optimization ==========
    if args.optimize:
        interactive_optimizer(code)
        sys.exit(0)

    # ========== Day 9: Explainable Test Generator ==========
    if args.testgen:
        generate_explainable_tests(code)
        sys.exit(0)

    # ========== Day 10: Refactor Explanation ==========
    if args.refactor_explain:
        explain_refactor_choices(code)
        sys.exit(0)

    # ========== Day 12: Predict Bugs ==========
    if args.predict_bugs:
        run_bug_prediction(code)
        sys.exit(0)

    # ========== Day 13: Security Check ==========
    if args.security_check:
        run_security_analysis(code)
        sys.exit(0)

    # ========== Day 1–2 Mentor (Pattern + RL + Neural) if user wants ==========

    if args.mentor:
        # We'll combine Day 1–2 logic in a single run:
        # RL or neural suggestions can be toggled by the flags.
        mentor = CodeMentor(use_neural=args.neural, use_rl=args.rl)
        if args.rl:
            raw_suggestions = mentor.analyze(code, return_raw=True)
            final_suggestions = []
            print("\nCode Mentor Suggestions (Day 1–2, RL mode):")
            for item in raw_suggestions:
                # RL feedback loop
                if isinstance(item, tuple) and item[0] != "neural":
                    idx, text = item
                    score = mentor.rl_agent.get_weight(idx)
                    print(f"Suggestion: {text} (score={score:.2f})")
                    while True:
                        try:
                            feedback = float(input("Rate this suggestion (0=bad, 1=good): "))
                            if feedback in [0,1]:
                                break
                            else:
                                print("Please enter 0 or 1.")
                        except ValueError:
                            print("Please enter a valid number (0 or 1).")
                    mentor.rl_agent.update(idx, feedback)
                    new_score = mentor.rl_agent.get_weight(idx)
                    final_suggestions.append(f"{text} (updated score={new_score:.2f})")
                elif isinstance(item, tuple) and item[0] == "neural":
                    # Neural suggestion
                    final_suggestions.append(f"Neural Suggestion: {item[1]}")
            print("\nFinal Suggestions (post-feedback):")
            for fs in final_suggestions:
                print(" -", fs)
        else:
            # Basic or neural only
            suggestions = mentor.analyze(code)
            print("\nCode Mentor Suggestions (Day 1–2):")
            for s in suggestions:
                print(" -", s)
        sys.exit(0)

    # If no flags provided:
    print("No flags provided. Use --help to see available options.")


if __name__ == "__main__":
    main()
