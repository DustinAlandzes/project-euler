import time

from problem07 import sieve_of_eratosthenes
from problem32 import is_pandigital

if __name__ == "__main__":
    start_time = time.time()
    primes = sieve_of_eratosthenes(7654321)
    pandigital_primes = []
    for prime in primes:
        if is_pandigital(prime, len(str(prime))):
            pandigital_primes.append(prime)
    print(max(pandigital_primes), time.time() - start_time)
