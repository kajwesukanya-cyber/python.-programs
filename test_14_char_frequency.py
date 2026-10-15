
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "14_char_frequency.py"
s = importlib.util.spec_from_file_location("char_frequency", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.char_frequency("hello") == {
    "h": 1, "e": 1, "l": 2, "o": 1
}
assert m.char_frequency("aaa") == {"a": 3}
assert m.char_frequency("") == {}

print("All test cases passed.")
