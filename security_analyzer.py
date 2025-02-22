import ast
from llm_handler import LLMAssistant

class SecurityAnalyzer:
    """
    Day 13: Identify security vulnerabilities in code and explain them symbolically.
    E.g., usage of 'exec', or insecure random, or hardcoded credentials.
    """
    def __init__(self, code):
        self.code = code
        self.vulnerabilities = []
        self.llm = LLMAssistant()

    def analyze_security(self):
        try:
            tree = ast.parse(self.code)
        except SyntaxError as e:
            self.vulnerabilities.append(f"SyntaxError: {str(e)}")
            return

        # 1. detect usage of 'exec'
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'exec':
                self.vulnerabilities.append("Use of 'exec' can lead to code injection vulnerabilities.")

        # 2. check for suspicious string patterns (like 'password=' or 'api_key=')
        if "password=" in self.code or "api_key=" in self.code:
            self.vulnerabilities.append("Hardcoded credentials found. This is a security risk.")

        # 3. detect usage of random without seed in certain contexts
        # (just an example, real checks would be more complex)

    def explain_vulnerabilities(self):
        """
        Uses LLM to produce a short explanation for each vulnerability.
        """
        if not self.vulnerabilities:
            return "No critical security vulnerabilities detected by symbolic analysis."

        prompt = f"""
We detected these possible security vulnerabilities:
{self.vulnerabilities}

Code:
{self.code}

Explain each vulnerability briefly, referencing best security practices.
"""
        return self.llm.generate_explanation(prompt)

def run_security_analysis(code):
    analyzer = SecurityAnalyzer(code)
    analyzer.analyze_security()
    explanation = analyzer.explain_vulnerabilities()
    print("\n=== Security Analysis ===\n", explanation)
