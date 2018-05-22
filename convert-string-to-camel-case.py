# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized.

# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):
    output = ''.join(x for x in text.title() if x not in "_-")
    return text[0] + output[1:] if text else ''
    
# Another solution using translate method

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
