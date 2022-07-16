# Use a numpy or pure python implementation
from prime_sieve.array import PrimeArraySieve

# from prime_sieve.list import PrimeListSieve

sieve = PrimeArraySieve()
# sieve = PrimeListSieve()

print(sieve.nth_prime(0))  # 2
print(sieve[4])  # 7
