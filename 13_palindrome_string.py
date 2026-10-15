
def palindrome_string(text):
    text = text.lower()
    return text == text[::-1]

assert palindrome_string("madam") == True
assert palindrome_string("hello") == False
assert palindrome_string("level") == True

print("All test cases passed.")
