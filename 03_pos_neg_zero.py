
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

assert check_number(5) == "Positive"
assert check_number(-3) == "Negative"
assert check_number(0) == "Zero"

print("All test cases passed.")
