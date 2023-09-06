# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    # Check if the input string is empty
    if not text:
        return ""

    words = re.split(r'[-_]', text)
    
    for i in range(len(words)):
        if i == 0:
            words[i] = words[i][0].upper() + words[i][1:] if words[i][0].isupper() else words[i]
        else:
            words[i] = words[i].capitalize()
    
    return ''.join(words)

# Example usage:
input_string1 = "The_Stealth-Warrior"
input_string2 = "the-stealth-warrior"
input_string3 = "Rhys-Is-A_cool-dude"

camel_case1 = to_camel_case(input_string1)
camel_case2 = to_camel_case(input_string2)
camel_case3 = to_camel_case(input_string3)

print(camel_case1)  # Output: "TheStealthWarrior"
print(camel_case2)  # Output: "theStealthWarrior"
print(camel_case3)  # Output: "rhysIsACoolDude"
