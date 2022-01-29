import parent_path
from my_functions import odd_even_to_number

"""
D: function: String=>Int     
Ex.  'Odd1' = 1, 'Even2' = 2 , 'Odd3' = 3, … 'Odd1Even2' = 12
"""

def test_odd1_to_1():
    assert odd_even_to_number('Odd1') == 1

def test_even2_to_2():
    assert odd_even_to_number('Even2') == 2

def test_odd3_to_3():
    assert odd_even_to_number('Odd3') == 3

def test_odd1_even2_to_12():
    assert odd_even_to_number('Odd1Even2') == 12

def test_even2_odd7_odd3_even_4_to_2734():
    assert odd_even_to_number('Even2Odd7Odd3Even4') == 2734