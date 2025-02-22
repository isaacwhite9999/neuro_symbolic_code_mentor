import ast
from llm_handler import LLMAssistant

class SemanticSearchEngine:
    """
    Day 16: Indexes code at an AST/semantic level, then uses LLM to interpret queries.
    """
    def __init__(self, code):
        self.code = code
        self.index = []
        self.assistant = LLMAssistant()

    def build_index(self):
        """
        Symbolically parse code, store function/class info. 
        """
        tree = ast.parse(self.code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                summary = f"Function: {node.name}"
                self.index.append(summary)
            if isinstance(node, ast.ClassDef):
                summary = f"Class: {node.name}"
                self.index.append(summary)

    def query_code(self, query):
        """
        Use an LLM to interpret the query, then do a simple match in self.index.
        """
        # Step 1: LLM helps refine query
        prompt = f"Refine this user query for code searching:\n{query}"
        refined = self.assistant.generate_explanation(prompt)

        # Step 2: match refined text in index (naive approach)
        results = []
        for entry in self.index:
            # simplistic partial match
            if any(word.lower() in entry.lower() for word in refined.split()):
                results.append(entry)
        return results

def run_semantic_search(code, user_query):
    engine = SemanticSearchEngine(code)
    engine.build_index()
    results = engine.query_code(user_query)
    print("\n=== Semantic Search (Day 16) ===\n")
    if results:
        print("Search Results:")
        for r in results:
            print(" -", r)
    else:
        print("No matches found.")
