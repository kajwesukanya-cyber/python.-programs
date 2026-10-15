
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "10_sum_of_digits.py"
s = importlib.util.spec_from_file_location("sum_digits", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.sum_digits(1234) == 10
assert m.sum_digits(567) == 18
assert m.sum_digits(0) == 0

print("All test cases passed.")
