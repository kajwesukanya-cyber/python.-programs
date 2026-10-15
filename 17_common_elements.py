
def common_elements(a, b):
    result = []

    for item in a:
        if item in b and item not in result:
            result.append(item)

    return result

assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
assert common_elements([5, 6], [6, 7]) == [6]
assert common_elements([1, 2], [3, 4]) == []

print("All test cases passed.")
