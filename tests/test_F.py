import parent_path
from my_functions import disordify_ddo_neve_words

"""
F: function: String=>String 
Ex.  '6868791'='DDO1', '786986692'='NEVE2', … '6868791786986692' = 'DDO1NEVE2' 
"""

def test_ddo1_disordinal():
    assert disordify_ddo_neve_words("6868791") == "DDO1"

def test_neve2_disordinal():
    assert disordify_ddo_neve_words("786986692") == "NEVE2"

def test_ddo1_neve2_disordinal():
    assert disordify_ddo_neve_words("6868791786986692") == "DDO1NEVE2"

def test_neve4_ddo9_neve6_disordinal():
    assert disordify_ddo_neve_words("7869866946868799786986696") == "NEVE4DDO9NEVE6"