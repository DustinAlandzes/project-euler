import time

from problem07 import sieve_of_eratosthenes

if __name__ == "__main__":
    """
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
    How many circular primes are there below one million?
    https://radiusofcircle.blogspot.com/2016/05/problem-35-project-euler-solution-with-python.html
    """
    start_time = time.time()
    primes = sieve_of_eratosthenes(1000000)
    count = 0
    for prime in primes:
        # assuming that there are no non-prime digits (2, 4, 6, 8, 5, 0)
        all_prime_digits = True

        # start with tens digit
        number = prime / 10

        # looping through digits
        while number:
            if (number % 10) % 2 == 0 or (number % 10) % 5 == 0:
                all_prime_digits = False
                break
            number //= 10

        if not all_prime_digits:
            continue
        length = len(str(prime))
        number = prime
        # assume that the circular permutations are prime
        count += 1
        # loop to create circular permutations
        for j in range(length):
            number = (number % 10) * 10 ** (length - 1) + number // 10
            # if any permutation is not prime
            if number not in primes:
                # subtract one from counter
                count -= 1
                break
    print(count, time.time() - start_time)
