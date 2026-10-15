
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

assert largest(10, 20, 15) == 20
assert largest(5, 2, 1) == 5
assert largest(3, 3, 2) == 3

print("All test cases passed.")
