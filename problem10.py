'''
Find the sum of all the primes below two million.
'''

# reusing this from problem 7
def sieve_of_eratosthenes(limit):
    '''
    Sieve of Eratosthenes
    A prime sieve works by creating a list of all integers up to a desired limit
    and progressively removing composite numbers (which it directly generates)
    until only primes are left

    time complexity: O(n log log n)
    space complexity: ?
    '''
    numbers = set(range(2, limit))

    for i in range(2, int(limit ** 0.5) + 1):
        for j in range(i * 2, limit, i):
            numbers.discard(j)

    return sorted(numbers)


def primes_below(n):
    return sieve_of_eratosthenes(n)


# the sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
assert sum(primes_below(10)) == 17

print(sum(primes_below(2000000)))
