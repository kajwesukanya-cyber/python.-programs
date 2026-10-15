
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

assert even_odd(4) == "Even"
assert even_odd(7) == "Odd"
assert even_odd(0) == "Even"

print("All test cases passed.")
