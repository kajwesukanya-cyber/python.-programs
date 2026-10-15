
def remove_duplicates(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
assert remove_duplicates([4, 4, 5]) == [4, 5]
assert remove_duplicates([]) == []

print("All test cases passed.")
