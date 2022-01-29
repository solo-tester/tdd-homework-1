import re

"""
A: function: Int=>String
Ex.  1 = 'Odd1', 2 = 'Even2', 3 = 'Odd3', … 12 = 'Odd1Even2'
"""
def number_to_string(num):
    num = int(num)
    if num == 0:
        return "Even0"

    nstr = ""
    last_digit = num%10

    if last_digit % 2 == 1:
        nstr = f"Odd{last_digit}"
    else:
        nstr = f"Even{last_digit}"

    num = int(num/10)

    if num == 0:
        return nstr
    else:
        return number_to_string(num) + nstr

"""
B: function: String=>String
* Ex.  'Odd1' = 'DDO1', 'Even2' = 'NEVE2' … 12 = 'DDO1NEVE2'
'Even6Odd5Even8' = 'NEVE6DDO5NEVE8'
"""
def reverse_odd_even_words(word):
    if len(word) == 0:
        return ""

    for i in range(len(word)):
        if re.match("[0-9]", word[i]):
            return word[i-1::-1].upper() + word[i] + reverse_odd_even_words(word[i+1::])


"""
C: function: String=>String 
Ex.  'DDO1' = '6868791', 'NEVE2' = '786986692', … 'Odd1Even2' = '6868791786986692'
"""
def ordify_ddo_neve_words(word):
    num_out = ""
    for c in word:
        if c.isnumeric():
            num_out += c
        else:
            num_out += str(ord(c))

    return num_out

"""
D: function: String=>Int     
Ex.  'Odd1' = 1, 'Even2' = 2 , 'Odd3' = 3, … 'Odd1Even2' = 12
"""
def odd_even_to_number(word):
    num_out = ""
    for c in word:
        if c.isnumeric():
            num_out += c
    return int(num_out)


"""
E: function: String=>String 
Ex.  'DDO1' = 'Odd1', 'NEVE2' = 'Even2'… 'DDO1NEVE2' = 'Odd1Even2'
"""
def reverse_ddo_neve_words(word):
    if len(word) == 0:
        return ""

    for i in range(len(word)):
        if re.match("[0-9]", word[i]):
            reversed_word = word[i-1::-1].lower().capitalize()
            return reversed_word + word[i] + reverse_ddo_neve_words(word[i+1::])


"""
F: function: String=>String 
Ex.  '6868791'='DDO1', '786986692'='NEVE2', … '6868791786986692' = 'DDO1NEVE2' 
"""
def disordify_ddo_neve_words(numbers):
    i = 0
    step = 2
    word = ""
    while i < len(numbers):
        beg = end = i
        if numbers[i] == '6':
            end = beg + 6
            for j in range(beg,end,step):
                num_slice = numbers[j:j+step]
                word += chr(int(num_slice))
            word += numbers[end]
            i += 7
        elif numbers[i] == '7':
            end = beg + 8
            for j in range(beg,end,step):
                num_slice = numbers[j:j+step]
                word += chr(int(num_slice))
            word += numbers[end]
            i += 9
    return word




# 68 D
# 79 O
# 78 N
# 69 E
# 86 V
"""
NEVE8DDO7
"""






















