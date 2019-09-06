from math import log, floor

from tools import measure_execution_time


def upper_bound_on_nth_prime(n):
    """ Comes from wikipedia:
    http://en.wikipedia.org/wiki/Prime-counting_function#Inequalities

    I took this from here:
    https://exercism.io/tracks/python/exercises/nth-prime/solutions/638fa55dca3c44d790a5b4e19573bed1
    https://codereview.stackexchange.com/questions/151095/get-nth-prime-number-using-sieve-of-eratosthenes/151226
    """
    if n <= 6:
        return 15
    else:
        return floor(n * log(n * log(n)))


def sieve_of_eratosthenes(limit):
    '''
    Sieve of Eratosthenes
    A prime sieve works by creating a list of all integers up to a desired limit
    and progressively removing composite numbers (which it directly generates)
    until only primes are left

    time complexity: O(n log log n)
    '''
    numbers = set(range(2, limit))

    for i in range(2, int(limit ** 0.5) + 1):
        for j in range(i * 2, limit, i):
            numbers.discard(j)

    return sorted(numbers)


@measure_execution_time
def nth_prime(n):
    # Make sure that the input makes sense
    if n < 1:
        raise ValueError("Input ({0}) must be greater than 0".format(n))

    # Get the upper bound using our nice function
    upper_bound = upper_bound_on_nth_prime(n)

    # Sieve on everything up to the upper bound
    primes = sieve_of_eratosthenes(upper_bound)

    # Grab the nth prime, which is n-1 on the list
    return primes[n - 1]


if __name__ == "__main__":
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.
    """
    assert nth_prime(6) == 13

    """
    What is the 10,001st prime number?
    """
    print(nth_prime(10001))
