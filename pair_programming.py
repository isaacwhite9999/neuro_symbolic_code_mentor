import ast
from llm_handler import LLMAssistant

class PairProgrammingAssistant:
    """
    Day 19: Interactive tool that listens to code changes 
    (simulated) and offers neuro-symbolic feedback in real-time.
    """
    def __init__(self):
        self.assistant = LLMAssistant()
        self.history = []

    def on_code_change(self, new_code):
        self.history.append(new_code)
        # Provide immediate suggestions
        prompt = f"""
We are pair-programming. The user just updated code to:
{new_code}

Provide immediate feedback or improvements using symbolic reasoning + LLM insights.
"""
        return self.assistant.generate_explanation(prompt)

def run_pair_programming_session():
    assistant = PairProgrammingAssistant()
    print("\n=== Real-Time Pair Programming (Day 19) ===\n")
    while True:
        code_update = input("Paste updated code (or 'quit'): ")
        if code_update.lower() == 'quit':
            break
        response = assistant.on_code_change(code_update)
        print("\nAssistant Feedback:\n", response)
