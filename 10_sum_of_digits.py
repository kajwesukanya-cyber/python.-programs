
def sum_digits(n):
    total = 0

    for digit in str(abs(n)):
        total += int(digit)

    return total

assert sum_digits(1234) == 10
assert sum_digits(567) == 18
assert sum_digits(0) == 0

print("All test cases passed.")
