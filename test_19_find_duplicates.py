
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "19_find_duplicates.py"
s = importlib.util.spec_from_file_location("find_duplicates", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.find_duplicates([1, 2, 2, 3, 1]) == [1, 2]
assert m.find_duplicates([4, 4, 5]) == [4]
assert m.find_duplicates([1, 2, 3]) == []

print("All test cases passed.")
