
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

assert is_prime(7) == True
assert is_prime(10) == False
assert is_prime(1) == False

print("All test cases passed.")
