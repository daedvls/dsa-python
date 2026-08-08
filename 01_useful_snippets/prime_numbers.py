import math

# one way to check if a number is prime
# check until sqrt(n)
# Useful if : checking only once or twice throughout the code
# NOTE: DON'T use this if you have to check multiple times throughout

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


# NOTE: If you have to check multiple times throughout the code, use the
# sieve of erathosthenes method. Generate a sieve once until the max possible n
# and then do O(1) access later

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for x in range(p * p, n + 1, p):
                is_prime[x] = False
        p += 1

    return is_prime

prime = sieve(10**6)  # say, the code gives constraint that n could be up to 10^6

print(prime[997])   # True
print(prime[1000])  # False