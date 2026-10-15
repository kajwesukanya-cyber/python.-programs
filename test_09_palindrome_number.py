
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "09_palindrome_number.py"
s = importlib.util.spec_from_file_location("palindrome_number", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.palindrome_number(121) == True
assert m.palindrome_number(123) == False
assert m.palindrome_number(1331) == True

print("All test cases passed.")
