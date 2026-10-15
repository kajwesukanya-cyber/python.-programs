
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "Code" / "13_palindrome_string.py"
s = importlib.util.spec_from_file_location("palindrome_string", p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)

assert m.palindrome_string("madam") == True
assert m.palindrome_string("hello") == False
assert m.palindrome_string("level") == True

print("All test cases passed.")
