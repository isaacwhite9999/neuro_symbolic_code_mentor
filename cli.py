import sys
import argparse
from dotenv import load_dotenv

# Days 1–13 imports (already existed):
from mentor import CodeMentor
from debugger import Debugger
from complexity import complexity_report
from refactor import symbolic_refactor
from review import review_code
from discussion import interactive_code_discussion
from code_optimizer import interactive_optimizer
from test_generator import generate_explainable_tests
from refactor_explainer import explain_refactor_choices
from version_control_assistant import interactive_merge_resolution
from static_bug_predictor import run_bug_prediction
from security_analyzer import run_security_analysis

# New Days 14–40 imports:
from day14_performance_profiler import run_performance_profiler
from day15_documentation_gen import run_documentation_generator
from day16_semantic_search import run_semantic_search
from day17_style_enforcer import enforce_style
from day18_code_summarizer import run_code_summarizer
from day19_pair_programming import run_pair_programming_session
from day20_error_pattern import run_error_pattern_recognition
from day21_modular_mentor import run_modular_mentor
from day22_algo_optimization import run_algo_optimization
from day23_legacy_refactor import run_legacy_refactor
from day24_quality_dashboard import run_quality_dashboard
from day25_expert_review_explainer import run_expert_review_explainer
from day26_future_issues import run_future_issues
from day27_library_updates import run_library_updates
from day28_coding_game import run_coding_game
from day29_error_correction import run_error_correction
from day30_runtime_optimizer import run_runtime_optimizer
from day31_feedback_mentor import run_feedback_mentor
from day32_dependency_graph import run_dependency_graph
from day33_refactor_benefits import run_refactor_benefits
from day34_snippet_generator import run_snippet_generator
from day35_coding_tutor import run_coding_tutor
from day36_commit_history import run_commit_history_analysis
from day37_code_translator import run_code_translator
from day38_api_usage import run_api_usage_analysis
from day39_data_structure import run_data_structure_optimizer
from day40_evaluation_suite import run_evaluation_suite


def get_code_input():
    print("Paste your Python code (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    return '\n'.join(lines)

def main():
    load_dotenv()  # loads .env for OPENAI_API_KEY, etc.

    parser = argparse.ArgumentParser(description="Neuro-Symbolic Code Mentor (Days 1–40)")

    # Existing flags from Days 1–13
    parser.add_argument("--mentor", action="store_true",
                        help="Day 1–2 Mentor: pattern matching + RL/Neural.")
    parser.add_argument("--rl", action="store_true", help="(Day 2) RL feedback for mentor.")
    parser.add_argument("--neural", action="store_true", help="(Day 1) Neural suggestions.")
    parser.add_argument("--debug", action="store_true", help="(Day 3) Symbolic debugging.")
    parser.add_argument("--interactive-debug", action="store_true", help="(Day 3) Debug w/ post-mortem.")
    parser.add_argument("--complexity", action="store_true", help="(Day 4) Cyclomatic complexity.")
    parser.add_argument("--refactor", action="store_true", help="(Day 5) Symbolic refactor.")
    parser.add_argument("--review", action="store_true", help="(Day 6) Automated code review.")
    parser.add_argument("--discussion", action="store_true", help="(Day 7) Interactive code discussion.")
    parser.add_argument("--optimize", action="store_true", help="(Day 8) Code optimization explorer.")
    parser.add_argument("--testgen", action="store_true", help="(Day 9) Explainable test generator.")
    parser.add_argument("--refactor-explain", action="store_true", help="(Day 10) Refactor explanation.")
    parser.add_argument("--merge-vcs", action="store_true", help="(Day 11) Merge resolution assistant.")
    parser.add_argument("--predict-bugs", action="store_true", help="(Day 12) Static bug prediction.")
    parser.add_argument("--security-check", action="store_true", help="(Day 13) Security analysis.")

    # New flags for Days 14–40:
    parser.add_argument("--perf-profile", action="store_true", help="(Day 14) Performance profiler.")
    parser.add_argument("--doc-gen", action="store_true", help="(Day 15) Documentation generator.")
    parser.add_argument("--semantic-search", action="store_true", help="(Day 16) Semantic code search.")
    parser.add_argument("--style-enforce", action="store_true", help="(Day 17) Style enforcer.")
    parser.add_argument("--code-summarize", action="store_true", help="(Day 18) Code summarizer.")
    parser.add_argument("--pair-prog", action="store_true", help="(Day 19) Real-time pair programming.")
    parser.add_argument("--error-pattern", action="store_true", help="(Day 20) Error pattern recognition.")
    parser.add_argument("--modular-mentor", action="store_true", help="(Day 21) Mentor for design patterns.")
    parser.add_argument("--algo-opt", action="store_true", help="(Day 22) Algorithm optimization.")
    parser.add_argument("--legacy-refactor", action="store_true", help="(Day 23) Legacy code refactoring.")
    parser.add_argument("--quality-dash", action="store_true", help="(Day 24) Code quality dashboard.")
    parser.add_argument("--expert-review", action="store_true", help="(Day 25) Explaining expert code reviews.")
    parser.add_argument("--future-issues", action="store_true", help="(Day 26) Predict future code issues.")
    parser.add_argument("--lib-updates", action="store_true", help="(Day 27) Library update suggestions.")
    parser.add_argument("--coding-game", action="store_true", help="(Day 28) Interactive coding game.")
    parser.add_argument("--error-correct", action="store_true", help="(Day 29) Real-time error correction.")
    parser.add_argument("--runtime-opt", action="store_true", help="(Day 30) Runtime perf optimization.")
    parser.add_argument("--feedback-mentor", action="store_true", help="(Day 31) Mentor w/ feedback on explanations.")
    parser.add_argument("--dep-graph", action="store_true", help="(Day 32) Dependency graph visualization.")
    parser.add_argument("--refactor-benefits", action="store_true", help="(Day 33) Predict refactor benefits.")
    parser.add_argument("--snippet-gen", action="store_true", help="(Day 34) Dynamic code snippet generator.")
    parser.add_argument("--coding-tutor", action="store_true", help="(Day 35) Intelligent coding tutor.")
    parser.add_argument("--commit-history", action="store_true", help="(Day 36) Analyze commit history.")
    parser.add_argument("--code-translator", action="store_true", help="(Day 37) Cross-language translator.")
    parser.add_argument("--api-usage", action="store_true", help="(Day 38) API usage analysis.")
    parser.add_argument("--data-struct-opt", action="store_true", help="(Day 39) Data structure optimization.")
    parser.add_argument("--eval-suite", action="store_true", help="(Day 40) Comprehensive evaluation suite.")

    args = parser.parse_args()

    # Special logic for Day 11 (merge two code branches):
    if args.merge_vcs:
        print("Paste code for branch A (END to finish):")
        branch_a = get_code_input()
        print("Paste code for branch B (END to finish):")
        branch_b = get_code_input()
        interactive_merge_resolution(branch_a, branch_b)
        sys.exit(0)

    # For Day 27, might need a different input for requirements, etc. We'll handle that below.
    # For the rest, we read a single code snippet.

    # If user selected library updates for Day 27, handle that first
    if args.lib_updates:
        print("Paste your requirements.txt content (END to finish):")
        lines = []
        while True:
            l = input()
            if l.strip().upper() == 'END':
                break
            lines.append(l)
        run_library_updates("\n".join(lines))
        sys.exit(0)

    # For day 37 code translator, we'll handle the custom input approach:
    if args.code_translator:
        from day37_code_translator import run_code_translator
        run_code_translator()
        sys.exit(0)

    # For the rest, we just read code from user
    code = get_code_input()

    # Existing day 1–2 mentor approach:
    if args.mentor:
        mentor = CodeMentor(use_neural=args.neural, use_rl=args.rl)
        if args.rl:
            raw_suggestions = mentor.analyze(code, return_raw=True)
            final_suggestions = []
            print("\nCode Mentor Suggestions (RL mode):")
            for item in raw_suggestions:
                if isinstance(item, tuple) and item[0] != "neural":
                    idx, text = item
                    score = mentor.rl_agent.get_weight(idx)
                    print(f"Suggestion: {text} (score={score:.2f})")
                    while True:
                        try:
                            fb = float(input("Rate this suggestion (0=bad,1=good): "))
                            if fb in [0,1]:
                                break
                            else:
                                print("Please enter 0 or 1.")
                        except ValueError:
                            print("Please enter a valid number (0 or 1).")
                    mentor.rl_agent.update(idx, fb)
                    new_score = mentor.rl_agent.get_weight(idx)
                    final_suggestions.append(f"{text} (updated score={new_score:.2f})")
                elif isinstance(item, tuple) and item[0] == "neural":
                    final_suggestions.append(f"Neural Suggestion: {item[1]}")
            print("\nFinal Suggestions (post-feedback):")
            for fs in final_suggestions:
                print(" -", fs)
        else:
            suggestions = mentor.analyze(code)
            print("\nCode Mentor Suggestions:")
            for s in suggestions:
                print(" -", s)
        sys.exit(0)

    # Day 3 debugging
    if args.debug or args.interactive_debug:
        dbg = Debugger(code)
        out = dbg.debug_code()
        print("\n=== Debugger (Day 3) ===\n", out)
        sys.exit(0)

    # Day 4 complexity
    if args.complexity:
        print("\n=== Complexity (Day 4) ===")
        print(complexity_report(code))
        sys.exit(0)

    # Day 5 refactor
    if args.refactor:
        new_code = symbolic_refactor(code)
        print("\n=== Refactored Code (Day 5) ===\n", new_code)
        sys.exit(0)

    # Day 6 review
    if args.review:
        print("\n=== Automated Review (Day 6) ===")
        out = review_code(code)
        print(out)
        sys.exit(0)

    # Day 7 discussion
    if args.discussion:
        interactive_code_discussion(code)
        sys.exit(0)

    # Day 8 optimize
    if args.optimize:
        interactive_optimizer(code)
        sys.exit(0)

    # Day 9 test generator
    if args.testgen:
        generate_explainable_tests(code)
        sys.exit(0)

    # Day 10 refactor explain
    if args.refactor_explain:
        explain_refactor_choices(code)
        sys.exit(0)

    # Day 12 predict bugs
    if args.predict_bugs:
        run_bug_prediction(code)
        sys.exit(0)

    # Day 13 security check
    if args.security_check:
        run_security_analysis(code)
        sys.exit(0)

    # ========== Days 14–40 ==========

    if args.perf_profile:  # Day 14
        run_performance_profiler(code)
        sys.exit(0)

    if args.doc_gen:  # Day 15
        run_documentation_generator(code)
        sys.exit(0)

    if args.semantic_search:  # Day 16
        user_query = input("Enter your search query: ")
        from day16_semantic_search import run_semantic_search
        run_semantic_search(code, user_query)
        sys.exit(0)

    if args.style_enforce:  # Day 17
        enforce_style(code)
        sys.exit(0)

    if args.code_summarize:  # Day 18
        run_code_summarizer(code)
        sys.exit(0)

    if args.pair_prog:  # Day 19
        from day19_pair_programming import run_pair_programming_session
        run_pair_programming_session()
        sys.exit(0)

    if args.error_pattern:  # Day 20
        tb_str = code  # interpret the pasted text as a traceback
        from day20_error_pattern import run_error_pattern_recognition
        run_error_pattern_recognition(tb_str)
        sys.exit(0)

    if args.modular_mentor:  # Day 21
        run_modular_mentor(code)
        sys.exit(0)

    if args.algo_opt:  # Day 22
        run_algo_optimization(code)
        sys.exit(0)

    if args.legacy_refactor:  # Day 23
        print("Paste historical JSON data (END to finish):")
        lines = []
        while True:
            l = input()
            if l.strip().upper() == 'END':
                break
            lines.append(l)
        run_legacy_refactor(code, "\n".join(lines))
        sys.exit(0)

    if args.quality_dash:  # Day 24
        run_quality_dashboard(code)
        sys.exit(0)

    if args.expert_review:  # Day 25
        print("Paste the expert review text (END to finish):")
        lines = []
        while True:
            l = input()
            if l.strip().upper() == 'END':
                break
            lines.append(l)
        run_expert_review_explainer(code, "\n".join(lines))
        sys.exit(0)

    if args.future_issues:  # Day 26
        run_future_issues(code)
        sys.exit(0)

    if args.coding_game:  # Day 28
        from day28_coding_game import run_coding_game
        run_coding_game()
        sys.exit(0)

    if args.error_correct:  # Day 29
        from day29_error_correction import run_error_correction
        run_error_correction()
        sys.exit(0)

    if args.runtime_opt:  # Day 30
        run_runtime_optimizer(code)
        sys.exit(0)

    if args.feedback_mentor:  # Day 31
        from day31_feedback_mentor import run_feedback_mentor
        run_feedback_mentor(code)
        sys.exit(0)

    if args.dep_graph:  # Day 32
        run_dependency_graph(code)
        sys.exit(0)

    if args.refactor_benefits:  # Day 33
        run_refactor_benefits(code)
        sys.exit(0)

    if args.snippet_gen:  # Day 34
        from day34_snippet_generator import run_snippet_generator
        run_snippet_generator()
        sys.exit(0)

    if args.coding_tutor:  # Day 35
        from day35_coding_tutor import run_coding_tutor
        run_coding_tutor()
        sys.exit(0)

    if args.commit_history:  # Day 36
        print("Paste commit history JSON (END to finish):")
        lines = []
        while True:
            l = input()
            if l.strip().upper() == 'END':
                break
            lines.append(l)
        run_commit_history_analysis("\n".join(lines))
        sys.exit(0)

    # code_translator done above for day 37

    if args.api_usage:  # Day 38
        print("Enter known API signatures as JSON (END to finish):")
        lines = []
        while True:
            l = input()
            if l.strip().upper() == 'END':
                break
            lines.append(l)
        from day38_api_usage import run_api_usage_analysis
        run_api_usage_analysis(code, {})  # parse or pass a dict
        sys.exit(0)

    if args.data_struct_opt:  # Day 39
        run_data_structure_optimizer(code)
        sys.exit(0)

    if args.eval_suite:  # Day 40
        run_evaluation_suite(code)
        sys.exit(0)

    print("No flags provided. Use --help to see all available options.")

if __name__ == "__main__":
    main()
