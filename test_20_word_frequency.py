
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "20_word_frequency.py"
s = importlib.util.spec_from_file_location("word_frequency", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.word_frequency("hello hello world") == {
    "hello": 2, "world": 1
}
assert m.word_frequency("Python is easy") == {
    "python": 1, "is": 1, "easy": 1
}
assert m.word_frequency("") == {}

print("All test cases passed.")
