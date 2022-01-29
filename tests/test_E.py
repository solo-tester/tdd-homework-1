import parent_path
from my_functions import reverse_ddo_neve_words

"""
E: function: String=>String 
Ex.  'DDO1' = 'Odd1', 'NEVE2' = 'Even2'… 'DDO1NEVE2' = 'Odd1Even2'
"""

def test_ddo1_to_odd1():
    assert reverse_ddo_neve_words('DDO1') == 'Odd1'

def test_neve2_to_even2():
    assert reverse_ddo_neve_words('NEVE2') == 'Even2'

def test_ddo1_neve2_to_odd1_even2():
    assert reverse_ddo_neve_words('DDO1NEVE2') == 'Odd1Even2'

def test_neve6_ddo5_neve8_to_even6_odd5_even8():
    assert reverse_ddo_neve_words('NEVE6DDO5NEVE8') == 'Even6Odd5Even8'