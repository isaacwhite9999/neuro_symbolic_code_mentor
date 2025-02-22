import re
from llm_handler import LLMAssistant

STYLE_RULES = {
    r"^\s*def [a-zA-Z0-9_]+\(.*\):\s*#.*": "Avoid inline comments on function definition lines",
    # Add more PEP-8 or custom style rules...
}

class StyleEnforcer:
    """
    Day 17: Checks code style with regex or symbolic rules, 
    then calls LLM for an explanation of each violation.
    """
    def __init__(self, code):
        self.code = code.splitlines()
        self.assistant = LLMAssistant()

    def check_style(self):
        violations = []
        for i, line in enumerate(self.code):
            for pattern, note in STYLE_RULES.items():
                if re.search(pattern, line):
                    violations.append((i+1, line.strip(), note))
        return violations

    def explain_violations(self, violations):
        if not violations:
            return "No style violations found."
        prompt = f"""
The following style violations were found in the code:
{violations}

Explain why each is a violation and how to fix it, referencing style best practices.
"""
        return self.assistant.generate_explanation(prompt)

def enforce_style(code):
    enforcer = StyleEnforcer(code)
    violations = enforcer.check_style()
    explanation = enforcer.explain_violations(violations)
    print("\n=== Style Enforcement (Day 17) ===\n", explanation)
