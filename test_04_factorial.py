
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "04_factorial.py"
s = importlib.util.spec_from_file_location("factorial", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.factorial(5) == 120
assert m.factorial(4) == 24
assert m.factorial(0) == 1

print("All test cases passed.")
