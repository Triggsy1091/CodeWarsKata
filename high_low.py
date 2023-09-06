def high_and_low(numbers):
    nums_list = [int(i) for i in numbers.split()]
    high = str(max(nums_list))
    low = str(min(nums_list))
    high_low = "{high} {low}".format(high = high, low = low)
    print(high_low)

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")