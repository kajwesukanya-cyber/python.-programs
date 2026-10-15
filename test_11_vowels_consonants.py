
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "11_vowels_consonants.py"
s = importlib.util.spec_from_file_location("vowels_consonants", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.count_vowels_consonants("Hello") == (2, 3)
assert m.count_vowels_consonants("Apple") == (2, 3)
assert m.count_vowels_consonants("AEIOU") == (5, 0)

print("All test cases passed.")
