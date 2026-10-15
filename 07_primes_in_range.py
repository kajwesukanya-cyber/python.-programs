
def primes_in_range(start, end):
    primes = []

    for n in range(start, end + 1):
        if n >= 2:
            prime = True

            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break

            if prime:
                primes.append(n)

    return primes

assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(10, 15) == [11, 13]

print("All test cases passed.")
