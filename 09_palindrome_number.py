
def palindrome_number(n):
    return n >= 0 and str(n) == str(n)[::-1]

assert palindrome_number(121) == True
assert palindrome_number(123) == False
assert palindrome_number(1331) == True

print("All test cases passed.")
