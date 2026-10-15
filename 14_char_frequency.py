
def char_frequency(text):
    frequency = {}

    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency

assert char_frequency("hello") == {
    "h": 1, "e": 1, "l": 2, "o": 1
}
assert char_frequency("aaa") == {"a": 3}

print("All test cases passed.")
