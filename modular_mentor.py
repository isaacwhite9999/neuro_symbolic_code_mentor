from llm_handler import LLMAssistant

DESIGN_PATTERNS = {
    "singleton": "Ensures a class has only one instance but can be a hidden dependency.",
    "factory": "Creates objects without specifying exact classes, but can complicate code with extra abstraction.",
    # ...
}

class ModularCodeMentor:
    """
    Day 21: Explains design pattern trade-offs symbolically.
    """
    def __init__(self, code):
        self.code = code
        self.assistant = LLMAssistant()

    def detect_design_patterns(self):
        # Very naive approach: look for keywords
        found = []
        for dp in DESIGN_PATTERNS:
            if dp in self.code.lower():
                found.append(dp)
        return found

    def explain_tradeoffs(self, patterns):
        prompt = f"""
We found these potential design patterns: {patterns}
Code:
{self.code}

Explain the trade-offs for each pattern in detail, referencing best practices.
"""
        return self.assistant.generate_explanation(prompt)

def run_modular_mentor(code):
    mm = ModularCodeMentor(code)
    patterns = mm.detect_design_patterns()
    explanation = mm.explain_tradeoffs(patterns)
    print("\n=== Modular Code Mentor (Day 21) ===\n", explanation)
