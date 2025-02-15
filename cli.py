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
Step 3: Review the suggestions and improve your code accordingly.
Step 4: Experiment by enabling or disabling neural suggestions with the '--neural' flag.

Usage Examples:
    Analyze a file:
        code-mentor path/to/your_code.py

    Enable neural suggestions:
        code-mentor --neural path/to/your_code.py

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
    parser.add_argument(
        "filepath",
        nargs="?",
        type=str,
        help="Path to the Python file to analyze."
    )
    parser.add_argument("--tutorial", action="store_true", help="Show interactive tutorial")
    parser.add_argument("--neural", action="store_true", help="Enable neural suggestions")
    parser.add_argument("--web", action="store_true", help="Run the web interface")
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
    
    mentor = CodeMentor(use_neural=args.neural)
    suggestions = mentor.analyze(code)
    
    if suggestions:
        print("\nCode Mentor Suggestions:")
        for idx, suggestion in enumerate(suggestions, start=1):
            print(f"{idx}. {suggestion}")
    else:
        print("All clear—no issues detected!")

if __name__ == "__main__":
    main()
