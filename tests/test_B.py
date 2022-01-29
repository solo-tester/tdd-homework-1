import parent_path
from my_functions import reverse_odd_even_words

"""
B: function: String=>String
* Ex.  'Odd1' = 'DDO1', 'Even2' = 'NEVE2' … 'Odd1Even2' = 'DDO1NEVE2'
"""

def test_odd1_to_ddo1():
    assert reverse_odd_even_words('Odd1') == 'DDO1'

def test_even2_to_neve2():
    assert reverse_odd_even_words('Even2') == 'NEVE2'

def test_odd1_even2_to_ddo1_neve2():
    assert reverse_odd_even_words('Odd1Even2') == 'DDO1NEVE2'

def test_even6_odd5_even8_to_neve6_ddo5_neve8():
    assert reverse_odd_even_words('Even6Odd5Even8') == 'NEVE6DDO5NEVE8'
