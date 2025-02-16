# neuro_symbolic_code_mentor/cli.py
import argparse
import sys

# Existing Day 1 & 2 imports
from neuro_symbolic_code_mentor.mentor import CodeMentor

def print_tutorial():
    tutorial_text = """
Interactive Tutorial for Neuro-Symbolic Code Mentor
----------------------------------------------------

Features (Days 1–5):
  1. Symbolic Pattern Matching (Day 1)
  2. Neural Suggestions (Day 1, optional)
  3. Reinforcement Learning (Day 2) - rates suggestions and prioritizes them over time
  4. Symbolic Debugging Assistant (Day 3) - explains errors, offers minimal fixes
  5. Code Complexity Analysis (Day 4) - calculates cyclomatic complexity of functions
  6. Code Refactoring (Day 5) - automatically improves code structure

Usage Examples:
  - Analyze a file with patterns + optional RL:
      code-mentor path/to/your_code.py
      code-mentor --rl path/to/your_code.py

  - Enable neural suggestions:
      code-mentor --neural path/to/your_code.py

  - Symbolic Debugging:
      code-mentor --debug path/to/your_code.py
      code-mentor --interactive-debug path/to/your_code.py

  - Complexity Analysis:
      code-mentor --complexity path/to/your_code.py

  - Code Refactoring:
      code-mentor --refactor path/to/your_code.py

  - Web Interface:
      code-mentor --web

  - Show this tutorial:
      code-mentor --tutorial
    """
    print(tutorial_text)

def main():
    parser = argparse.ArgumentParser(
        description="Neuro-Symbolic Code Mentor: Analyze Python code with pattern matching, RL, debugging, complexity, and refactoring."
    )
    parser.add_argument("filepath", nargs="?", type=str, help="Path to the Python file to analyze.")
    parser.add_argument("--tutorial", action="store_true", help="Show interactive tutorial")
    parser.add_argument("--neural", action="store_true", help="Enable neural suggestions")
    parser.add_argument("--rl", action="store_true", help="Enable reinforcement learning feedback")
    parser.add_argument("--web", action="store_true", help="Run the web interface")

    # Day 3: Debugging
    parser.add_argument("--debug", action="store_true", help="Run the symbolic debugging assistant")
    parser.add_argument("--interactive-debug", action="store_true", help="Symbolic debugger with post-mortem debugging")

    # Day 4: Complexity
    parser.add_argument("--complexity", action="store_true", help="Analyze cyclomatic complexity of code functions")

    # Day 5: Refactoring
    parser.add_argument("--refactor", action="store_true", help="Automatically refactor code and print the new version")

    args = parser.parse_args()

    # Handle tutorial
    if args.tutorial:
        print_tutorial()
        return

    # Handle web interface
    if args.web:
        from neuro_symbolic_code_mentor.web_app import app
        app.run(debug=True)
        return

    # Ensure a filepath is provided unless tutorial/web is selected
    if not args.filepath:
        parser.print_help()
        return

    # Attempt to read code file
    try:
        with open(args.filepath, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

    # Day 4: Complexity
    if args.complexity:
        from neuro_symbolic_code_mentor.complexity import complexity_report
        print("\nCode Complexity Analysis:\n")
        print(complexity_report(code))
        return

    # Day 3: Debugging
    if args.debug or args.interactive_debug:
        from neuro_symbolic_code_mentor.debugger import debug_code
        result = debug_code(code, interactive=args.interactive_debug)
        print(result)
        return

    # Day 5: Refactoring
    if args.refactor:
        from neuro_symbolic_code_mentor.refactor import symbolic_refactor, neural_refactor_docstrings

        print("\nApplying symbolic refactoring...")
        new_code = symbolic_refactor(code)

        # Optionally chain neural docstring improvements:
        # new_code = neural_refactor_docstrings(new_code)

        print("\nRefactored Code:\n")
        print(new_code)
        return

    # Otherwise, default to Day 1 & 2 Mentor Analysis
    mentor = CodeMentor(use_neural=args.neural, use_rl=args.rl)

    # RL logic => interactive feedback
    if args.rl:
        raw_suggestions = mentor.analyze(code, return_raw=True)
        final_suggestions = []
        print("\nCode Mentor Suggestions:")
        for item in raw_suggestions:
            if isinstance(item, tuple) and item[0] != "neural":
                pattern_idx, suggestion = item
                score = mentor.rl_agent.get_weight(pattern_idx)
                print(f"Suggestion: {suggestion} (current score: {score:.2f})")
                while True:
                    try:
                        feedback = float(input("Rate this suggestion (0 = bad, 1 = good): "))
                        if feedback in [0, 1]:
                            break
                        else:
                            print("Please enter 0 or 1.")
                    except ValueError:
                        print("Please enter a valid number (0 or 1).")
                mentor.rl_agent.update(pattern_idx, feedback)
                updated_score = mentor.rl_agent.get_weight(pattern_idx)
                print(f"Updated score: {updated_score:.2f}\n")
                final_suggestions.append(f"{suggestion} (score: {updated_score:.2f})")
            elif isinstance(item, tuple) and item[0] == "neural":
                final_suggestions.append(f"Neural Suggestion: {item[1]}")

        print("\nFinal Suggestions (post-feedback):")
        for idx, sugg in enumerate(final_suggestions, start=1):
            print(f"{idx}. {sugg}")

    else:
        # Non-RL path => just get a list of suggestions
        suggestions = mentor.analyze(code)
        if suggestions:
            print("\nCode Mentor Suggestions:")
            for idx, suggestion in enumerate(suggestions, start=1):
                print(f"{idx}. {suggestion}")
        else:
            print("All clear—no issues detected!")

if __name__ == "__main__":
    main()
