
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "06_prime_number.py"
s = importlib.util.spec_from_file_location("prime", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.is_prime(7) == True
assert m.is_prime(10) == False
assert m.is_prime(1) == False

print("All test cases passed.")
