
def missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(numbers)

assert missing_number([1, 2, 4, 5]) == 3
assert missing_number([1, 3, 4, 5]) == 2
assert missing_number([2, 3, 4, 5]) == 1

print("All test cases passed.")
