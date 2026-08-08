import math

# most efficient way to check if a number is prime
# check until sqrt(n)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = math.isqrt(n)   # integer square root
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True