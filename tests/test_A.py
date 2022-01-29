import parent_path
from my_functions import number_to_string

"""
A: function: Int=>String
Ex.  1 = 'Odd1', 2 = 'Even2', 3 = 'Odd3', … 12 = 'Odd1Even2'
"""

def test_10_is_odd1_even0():
    assert number_to_string(10) == 'Odd1Even0'

def test_0_is_even0():
    assert number_to_string(0) == 'Even0'

def test_1_is_odd1():
    assert number_to_string(1) == 'Odd1'

def test_2_is_even2():
    assert number_to_string(2) == 'Even2'

def test_3_is_odd3():
    assert number_to_string(3) == 'Odd3'

def test_12_is_odd1_even2():
    assert number_to_string(12) == 'Odd1Even2'

def test_245_is_odd1_even2():
    assert number_to_string(245) == 'Even2Even4Odd5'