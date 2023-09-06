def square_digits(num):
    # Your code here
    digits = [d for d in str(num)]
    # print(digits)
    
    result = list(map(lambda x: int(x) ** 2, digits))
    squared_values = ''.join(result)
    return squared_values

# square_digits(9119)
print(square_digits(9119))