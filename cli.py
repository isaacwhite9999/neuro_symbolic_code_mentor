# neuro_symbolic_code_mentor/cli.py

import argparse
import sys
from neuro_symbolic_code_mentor.mentor import CodeMentor

def print_tutorial():
    tutorial_text = """
Interactive Tutorial for Neuro-Symbolic Code Mentor
----------------------------------------------------

Step 1: Provide your Python code via a file (CLI mode) or through the web interface.
Step 2: The tool analyzes your code using:
    - Symbolic Pattern Matching: Flags common coding pitfalls.
    - Neural Text Generation: Provides context-aware advice.
    - Reinforcement Learning (optional): Adapts suggestion rankings based on your feedback.
Step 3: Review the suggestions, and if RL is enabled, rate each suggestion (0 = bad, 1 = good).
Step 4: The system will update the suggestion scores based on your feedback.
Step 5: Experiment by enabling or disabling neural and RL features with the '--neural' and '--rl' flags.

Usage Examples:
    Analyze a file:
        code-mentor path/to/your_code.py

    Enable neural suggestions:
        code-mentor --neural path/to/your_code.py

    Enable reinforcement learning feedback:
        code-mentor --rl path/to/your_code.py

    Run the web interface:
        code-mentor --web

    Show this tutorial:
        code-mentor --tutorial
    """
    print(tutorial_text)

def main():
    parser = argparse.ArgumentParser(
        description="Neuro-Symbolic Code Mentor: Analyze your Python code for common pitfalls."
    )
    parser.add_argument("filepath", nargs="?", type=str, help="Path to the Python file to analyze.")
    parser.add_argument("--tutorial", action="store_true", help="Show interactive tutorial")
    parser.add_argument("--neural", action="store_true", help="Enable neural suggestions")
    parser.add_argument("--web", action="store_true", help="Run the web interface")
    parser.add_argument("--rl", action="store_true", help="Enable reinforcement learning feedback")
    args = parser.parse_args()
    
    if args.tutorial:
        print_tutorial()
        return
    
    if args.web:
        from neuro_symbolic_code_mentor.web_app import app
        app.run(debug=True)
        return
    
    if not args.filepath:
        parser.print_help()
        return
    
    try:
        with open(args.filepath, "r", encoding="utf-8") as file:
            code = file.read()
    except Exception as e:
        sys.exit(f"Error reading file: {e}")
    
    mentor = CodeMentor(use_neural=args.neural, use_rl=args.rl)
    
    # If RL feedback is enabled, run interactive feedback loop.
    if args.rl:
        raw_suggestions = mentor.analyze(code, return_raw=True)
        final_suggestions = []
        print("\nCode Mentor Suggestions:")
        for item in raw_suggestions:
            # Process symbolic suggestions (tuple format)
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
            # Process neural suggestion (do not collect feedback)
            elif isinstance(item, tuple) and item[0] == "neural":
                final_suggestions.append(f"Neural Suggestion: {item[1]}")
        
        print("\nFinal Suggestions (post-feedback):")
        for idx, suggestion in enumerate(final_suggestions, start=1):
            print(f"{idx}. {suggestion}")
    else:
        suggestions = mentor.analyze(code)
        if suggestions:
            print("\nCode Mentor Suggestions:")
            for idx, suggestion in enumerate(suggestions, start=1):
                print(f"{idx}. {suggestion}")
        else:
            print("All clear—no issues detected!")

if __name__ == "__main__":
    main()

