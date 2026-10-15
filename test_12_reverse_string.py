
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "12_reverse_string.py"
s = importlib.util.spec_from_file_location("reverse_string", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.reverse_string("hello") == "olleh"
assert m.reverse_string("Python") == "nohtyP"
assert m.reverse_string("") == ""

print("All test cases passed.")
