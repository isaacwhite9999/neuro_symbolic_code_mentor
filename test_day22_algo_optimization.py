import pytest
from day22_algo_optimization import AlgorithmOptimizer

def test_analyze_algorithms():
    code = """
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
"""
    ao = AlgorithmOptimizer(code)
    pattern = ao.analyze_algorithms()
    assert "bubble sort" in pattern.lower()
