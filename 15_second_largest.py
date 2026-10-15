
def second_largest(numbers):
    unique = sorted(set(numbers), reverse=True)

    if len(unique) < 2:
        raise ValueError("Need two distinct numbers")

    return unique[1]

assert second_largest([10, 20, 30, 40]) == 30
assert second_largest([5, 5, 3, 1]) == 3
assert second_largest([8, 2, 6]) == 6

print("All test cases passed.")
