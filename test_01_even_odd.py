
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "01_even_odd.py"
s = importlib.util.spec_from_file_location("even_odd", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.even_odd(4) == "Even"
assert m.even_odd(7) == "Odd"
assert m.even_odd(0) == "Even"

print("All test cases passed.")
