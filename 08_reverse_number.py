
def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num

assert reverse_number(1234) == 4321
assert reverse_number(500) == 5
assert reverse_number(-123) == -321

print("All test cases passed.")
