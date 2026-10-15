
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "05_fibonacci_series.py"
s = importlib.util.spec_from_file_location("fibonacci", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.fibonacci(5) == [0, 1, 1, 2, 3]
assert m.fibonacci(6) == [0, 1, 1, 2, 3, 5]
assert m.fibonacci(0) == []

print("All test cases passed.")
