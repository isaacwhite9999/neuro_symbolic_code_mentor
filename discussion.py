from llm_handler import LLMAssistant
from symbolic_analyzer import SymbolicAnalyzer

def interactive_code_discussion(code):
    """
    Day 7: Combines a large language model (LLMAssistant) with symbolic analysis
    for interactive code Q&A.

    1. Runs symbolic analysis on the provided code.
    2. Displays detected symbolic issues to the user.
    3. Enters a loop where the user asks questions, and the LLM responds, referencing any symbolic issues if relevant.
    """
    assistant = LLMAssistant()
    analyzer = SymbolicAnalyzer(code)
    analyzer.analyze()

    # Print any symbolic issues
    if analyzer.issues:
        print("Symbolic issues found:")
        for issue in analyzer.issues:
            print(" -", issue)
    else:
        print("No symbolic issues detected.\n")

    # Interactive Q&A
    while True:
        question = input("\nAsk a question about your code (or type 'quit'): ")
        if question.lower() in ["quit", "exit"]:
            break

        # Build a prompt that combines code, symbolic issues, and user question
        prompt = f"""
        Code:
        {code}

        Symbolic Issues: {analyzer.issues}

        The user asks: {question}

        Provide a helpful, short explanation referencing these issues if relevant.
        """
        reply = assistant.generate_explanation(prompt)
        print("\nAI Response:\n", reply)
