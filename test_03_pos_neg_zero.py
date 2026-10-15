
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "03_pos_neg_zero.py"
s = importlib.util.spec_from_file_location("number", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.check_number(5) == "Positive"
assert m.check_number(-3) == "Negative"
assert m.check_number(0) == "Zero"

print("All test cases passed.")
