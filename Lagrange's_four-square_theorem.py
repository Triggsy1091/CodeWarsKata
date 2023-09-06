import math

def lagrange_four_square(n):
    if n < 0:
        return None  # Negative numbers are not included in the theorem

    # Find the integer square root of n
    sqrt_n = int(math.sqrt(n))

    # If n is already a perfect square, return it as one of the four squares
    if sqrt_n * sqrt_n == n:
        return [sqrt_n, 0, 0, 0]

    for a in range(sqrt_n, -1, -1):
        for b in range(a, -1, -1):
            for c in range(b, -1, -1):
                remainder = n - a*a - b*b - c*c
                if remainder >= 0:
                    d = int(math.sqrt(remainder))
                    if a*a + b*b + c*c + d*d == n:
                        return [a, b, c, d]

    return None  # No such representation found

# Example usage:
n = 25
representation = lagrange_four_square(n)
if representation:
    print(f"{n} can be represented as the sum of four squares: {representation}")
else:
    print(f"No representation found for {n}")