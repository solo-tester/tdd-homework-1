import parent_path
from my_functions import ordify_ddo_neve_words


"""
C: function: String=>String 
Ex.  'DDO1' = '6868791', 'NEVE2' = '786986692', … 'DDO1NEVE2' = '6868791786986692'
"""

def test_ddo1_ordinal():
    assert ordify_ddo_neve_words("DDO1") == "6868791"

def test_neve2_ordinal():
    assert ordify_ddo_neve_words("NEVE2") == "786986692"

def test_ddo1_neve2_ordinal():
    assert ordify_ddo_neve_words("DDO1NEVE2") == "6868791786986692"

def test_neve4_ddo9_neve6_ordinal():
    assert ordify_ddo_neve_words("NEVE4DDO9NEVE6") == "7869866946868799786986696"