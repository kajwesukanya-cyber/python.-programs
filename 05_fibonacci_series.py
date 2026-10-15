
def fibonacci(n):
    a, b = 0, 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series

assert fibonacci(5) == [0, 1, 1, 2, 3]
assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
assert fibonacci(0) == []

print("All test cases passed.")
