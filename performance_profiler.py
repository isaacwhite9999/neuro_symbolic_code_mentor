import time
import ast
from llm_handler import LLMAssistant

class PerformanceProfiler:
    """
    Day 14: Profiles code performance, highlights bottlenecks, then uses LLM to explain optimizations.
    """
    def __init__(self, code):
        self.code = code
        self.assistant = LLMAssistant()

    def run_profile(self):
        """
        Simple approach: time the execution of the code (or specific functions).
        Real approach might use cProfile or an AST-based function hooking.
        """
        start = time.time()
        try:
            exec(self.code, {})
        except Exception as e:
            return f"Runtime Error during profiling: {str(e)}"
        elapsed = time.time() - start
        return f"Execution Time: {elapsed:.4f} seconds"

    def explain_optimizations(self, timing):
        """
        LLM call to explain potential optimizations based on the code & timing result.
        """
        prompt = f"""
We profiled this code, which took about {timing}.
Code:
{self.code}

Suggest how to optimize any bottlenecks, providing symbolic reasoning for each suggestion.
"""
        return self.assistant.generate_explanation(prompt)

def run_performance_profiler(code):
    """
    Main Day 14 function: runs a simple performance test, then calls LLM for explanation.
    """
    profiler = PerformanceProfiler(code)
    timing_str = profiler.run_profile()
    if "Runtime Error" in timing_str:
        print(timing_str)
        return
    explanation = profiler.explain_optimizations(timing_str)
    print("\n=== Performance Profiler (Day 14) ===\n")
    print(timing_str)
    print("\nOptimizations:\n", explanation)
