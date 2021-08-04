from sympy import *

x = 0


def sum_of_unique_prime_factors(n):
    divisor = 2
    sum = 0
    last = 0
    while divisor <= n / 2:
        if (n % divisor) == 0:
            n = n / divisor
            if divisor != last:
                last = divisor
                sum = sum + divisor
        else:
            divisor = divisor + 1

    return sum if n == last else sum + n


for i in range(6, 20):
    x = i
    while x != 1:
        if not isprime(x):
            x = x - int(sum_of_unique_prime_factors(x))
        else:
            x = x * 2
