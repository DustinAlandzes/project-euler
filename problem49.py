from problem07 import sieve_of_eratosthenes


def is_permutation(a, b):
    """
    stolen from https://optimizer0528.tistory.com/114
    :param j:
    :param k:
    :return:
    """
    stra = sorted(str(a))
    strb = sorted(str(a))
    if stra == strb and strb == stra:
        return True


if __name__ == "__main__":
    """
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
    """
    # 4 digit primes
    primes = [prime for prime in sieve_of_eratosthenes(10000) if len(list(str(prime))) == 4]

    for key, prime in enumerate(primes):
        if len(list(str(prime))) < 4:
            continue
        next_primes = [primes[key + 1], primes[key + 2], primes[key + 3]]
        # for prime in primes:
        # if they are within
