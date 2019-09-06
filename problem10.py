import time

from problem07 import sieve_of_eratosthenes


def primes_below(n):
    return sieve_of_eratosthenes(n)


if __name__ == "__main__":
    # the sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    assert sum(primes_below(10)) == 17
    """
    Find the sum of all the primes below two million.
    """
    start_time = time.time()
    print(sum(primes_below(2000000)), time.time() - start_time)
