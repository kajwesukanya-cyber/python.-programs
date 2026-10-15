
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?;:")
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency

assert word_frequency("hello hello world") == {
    "hello": 2, "world": 1
}
assert word_frequency("Python is easy") == {
    "python": 1, "is": 1, "easy": 1
}

print("All test cases passed.")
