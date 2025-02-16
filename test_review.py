# tests/test_review.py

import pytest
from neuro_symbolic_code_mentor.review import generate_review_report

def test_review_end_to_end():
    code = \"\"\"\
def process_stuff(lst):
    if lst == None:
        print(\"Found None!\")
    for i in range(len(lst)):
        print(lst[i])

def big_boy(x):
    while x < 10:
        x += 1
        if x == 5:
            break
    return x
\"\"\"
    report = generate_review_report(code)
    # Check for pattern-based issues mention
    assert "potential issues" in report
    assert "lst == None" in report or "x == None" in report or "Found None!" in report
    # Check for complexity mention
    assert "big_boy" in report
    # Check for refactor suggestions mention
    assert "Symbolic Refactor Suggestions" in report
    # Maybe it should mention converting 'for i in range(len(lst)):' -> 'for item in lst:'
    assert "for item in lst" in report or "diff" in report
