
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "07_primes_in_range.py"
s = importlib.util.spec_from_file_location("primes_range", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.primes_in_range(1, 10) == [2, 3, 5, 7]
assert m.primes_in_range(10, 15) == [11, 13]
assert m.primes_in_range(14, 16) == []

print("All test cases passed.")
