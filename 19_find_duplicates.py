
def find_duplicates(numbers):
    duplicates = []

    for i in range(len(numbers)):
        if numbers[i] in numbers[i + 1:]:
            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])

    return duplicates

assert find_duplicates([1, 2, 2, 3, 1]) == [1, 2]
assert find_duplicates([4, 4, 5]) == [4]
assert find_duplicates([1, 2, 3]) == []

print("All test cases passed.")
