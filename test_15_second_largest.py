
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "15_second_largest.py"
s = importlib.util.spec_from_file_location("second_largest", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.second_largest([10, 20, 30, 40]) == 30
assert m.second_largest([5, 5, 3, 1]) == 3
assert m.second_largest([8, 2, 6]) == 6

print("All test cases passed.")
