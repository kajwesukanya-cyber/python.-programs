
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "18_missing_number.py"
s = importlib.util.spec_from_file_location("missing_number", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.missing_number([1, 2, 4, 5]) == 3
assert m.missing_number([1, 3, 4, 5]) == 2
assert m.missing_number([2, 3, 4, 5]) == 1

print("All test cases passed.")
