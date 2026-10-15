
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "16_remove_duplicates.py"
s = importlib.util.spec_from_file_location("remove_duplicates", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
assert m.remove_duplicates([4, 4, 5]) == [4, 5]
assert m.remove_duplicates([]) == []

print("All test cases passed.")
