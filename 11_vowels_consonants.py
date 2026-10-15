
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants

assert count_vowels_consonants("Hello") == (2, 3)
assert count_vowels_consonants("Apple") == (2, 3)
assert count_vowels_consonants("AEIOU") == (5, 0)

print("All test cases passed.")
