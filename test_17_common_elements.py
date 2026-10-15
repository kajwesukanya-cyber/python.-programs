
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "17_common_elements.py"
s = importlib.util.spec_from_file_location("common_elements", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
assert m.common_elements([5, 6], [6, 7]) == [6]
assert m.common_elements([1, 2], [3, 4]) == []

print("All test cases passed.")
