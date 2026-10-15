
def reverse_string(text):
    result = ""

    for ch in text:
        result = ch + result

    return result

assert reverse_string("hello") == "olleh"
assert reverse_string("Python") == "nohtyP"
assert reverse_string("") == ""

print("All test cases passed.")
