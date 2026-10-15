
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "08_reverse_number.py"
s = importlib.util.spec_from_file_location("reverse_number", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.reverse_number(1234) == 4321
assert m.reverse_number(500) == 5
assert m.reverse_number(-123) == -321

print("All test cases passed.")
