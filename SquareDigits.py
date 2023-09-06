# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 7^2 is 49, 6^2 is 36, and 5^2 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!

def square_digits(num):
    # Create a list containing the individual digits from num
    digits = [int(d) for d in str(num)]
    # Square Each Digit within the new list digits
    result = list(map(lambda x: int(x) ** 2, digits))
    # Use map() function to store the squared values as string, then create one string of all of the results
    squared_values = map(str, result)
    final_results = ''.join(squared_values)
    # return this string as an int as per rules
    return int(final_results)

# square_digits(9119)
print(square_digits(9119))