
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "02_largest_of_three.py"
s = importlib.util.spec_from_file_location("largest", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.largest(10, 20, 15) == 20
assert m.largest(5, 2, 1) == 5
assert m.largest(3, 3, 2) == 3

print("All test cases passed.")
