
import pytest
from neuro_symbolic_code_mentor.complexity import analyze_complexity, complexity_report, COMPLEXITY_THRESHOLD

def test_simple_function():
    code = \"\"\"\
def foo():
    return 42
\"\"\"
    results = analyze_complexity(code)
    assert results.get('foo') == 1, "A simple function should have complexity 1."

def test_branching():
    code = \"\"\"\
def bar(x):
    if x > 0:
        print(\"pos\")
    else:
        print(\"neg\")
\"\"\"
    results = analyze_complexity(code)
    # 1 base + 1 if => 2
    assert results.get('bar') == 2, \"One 'if' statement => complexity = 2.\"

def test_complex_function():
    code = \"\"\"\
def complex_func(x):
    for i in range(x):
        if i % 2 == 0:
            print(i)
        else:
            print(\"Odd\")
    while x < 100:
        x += 10
        if x % 3 == 0:
            break
    return x
\"\"\"
    results = analyze_complexity(code)
    score = results.get('complex_func')
    assert score >= 6, f\"Expected complexity of at least 6, got {score}.\"

def test_report():
    code = \"\"\"\
def big_one(n):
    for i in range(n):
        if i < 10:
            print(i)
        else:
            print(\"over 10\")
    while n > 0:
        n -= 1
        if n == 5:
            break
\"\"\"
    report_str = complexity_report(code)
    assert \"Function 'big_one' has COMPLEXITY=\" in report_str, \"Expected a complexity report line.\"

def test_exceed_threshold():
    code = \"\"\"\
def insane_func(a, b):
    if a > b:
        print(\"a > b\")
    for i in range(5):
        if i % 2 == 0:
            while i < 10:
                i += 1
                if i == 5:
                    break
                else:
                    a += i
    # Additional branching
    if a == 1:
        print(\"One\")
    if a == 2:
        print(\"Two\")
    if a == 3:
        print(\"Three\")
\"\"\"
    rep = complexity_report(code)
    # We expect it to exceed COMPLEXITY_THRESHOLD=10
    assert \"Consider refactoring!\" in rep, \"Function should exceed complexity threshold.\"
