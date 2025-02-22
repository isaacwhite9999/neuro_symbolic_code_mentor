import re
from llm_handler import LLMAssistant

COMMON_ERRORS = {
    r"ZeroDivisionError": "Guide: Check your denominator before dividing.",
    r"IndexError": "Guide: Ensure list/array indices are in range.",
    # etc.
}

class ErrorPatternRecognizer:
    """
    Day 20: Looks for known error patterns in tracebacks, 
    then provides symbolic troubleshooting steps.
    """
    def __init__(self, traceback_str):
        self.traceback_str = traceback_str
        self.llm = LLMAssistant()

    def find_patterns(self):
        suggestions = []
        for pattern, guide in COMMON_ERRORS.items():
            if re.search(pattern, self.traceback_str):
                suggestions.append(guide)
        return suggestions

    def symbolic_troubleshoot(self):
        patterns = self.find_patterns()
        if not patterns:
            return "No known error patterns found."
        prompt = f"""
We found these known error patterns: {patterns}
Traceback:
{self.traceback_str}

Provide a short symbolic troubleshooting guide.
"""
        return self.llm.generate_explanation(prompt)

def run_error_pattern_recognition(traceback_str):
    epr = ErrorPatternRecognizer(traceback_str)
    result = epr.symbolic_troubleshoot()
    print("\n=== Error Pattern Recognition (Day 20) ===\n", result)
