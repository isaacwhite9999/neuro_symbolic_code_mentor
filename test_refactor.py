# tests/test_refactor.py

import pytest
from neuro_symbolic_code_mentor.refactor import symbolic_refactor

def test_none_comparison():
    code = \"\"\"\
def check_none(x):
    if x == None:
        return True
    else:
        return False
\"\"\"
    refactored = symbolic_refactor(code)
    # We expect 'x == None' => 'x is None'
    assert 'x is None' in refactored, \"Should replace 'x == None' with 'x is None'.\"

def test_bool_comparison():
    code = \"\"\"\
def check_bool(x):
    if x == True:
        return 'yes'
    if x == False:
        return 'no'
\"\"\"
    refactored = symbolic_refactor(code)
    # x == True => x
    # x == False => not x
    assert 'if x:' in refactored
    assert 'if not x:' in refactored

def test_for_range_len():
    code = \"\"\"\
def iterate_list(my_list):
    for i in range(len(my_list)):
        print(my_list[i])
\"\"\"
    refactored = symbolic_refactor(code)
    # Should replace 'for i in range(len(my_list)):' with 'for item in my_list:'
    assert 'for item in my_list:' in refactored, \"Should replace index-based iteration with direct iteration.\"
    # And ensure 'my_list[i]' turned into 'item'
    assert 'print(item)' in refactored

def test_no_change():
    # No changes needed
    code = \"\"\"\
def do_nothing(a):
    return a + 1
\"\"\"
    refactored = symbolic_refactor(code)
    # Should remain the same
    assert refactored.strip() == code.strip()
