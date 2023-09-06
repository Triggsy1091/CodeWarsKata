import re

def to_camel_case(input_string):
    # Split the input string by hyphens and underscores
    words = re.split(r'[-_]', input_string)
    
    # Capitalize the first word if it was already capitalized
    if words and words[0][0].isupper():
        words[0] = words[0][0].upper() + words[0][1:]
    
    # Capitalize the remaining words
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()

    # Join the words to form the CamelCase string
    camel_case_string = ''.join(words)

    return camel_case_string

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
