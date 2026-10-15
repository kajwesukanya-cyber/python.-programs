
def factorial(n):
    if n < 0:
        raise ValueError("Number must be non-negative")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

assert factorial(5) == 120
assert factorial(4) == 24
assert factorial(0) == 1

print("All test cases passed.")
