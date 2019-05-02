"""
Find the smallest denominator
having a resilience < 15499/94744
"""
import fractions

import eulerlib
import math


# al prime numbers have a resilience of 1
#
def resilience(denominator):
    proper_fractions = []
    for x in range(denominator):
        proper_fractions.append((x, denominator))
    # see which of the proper fractions can be cancelled down


def is_prime(num):
    # type(int) -> bool
    """
    returns primality of number
    """
    if num < 2:
        return False
    if num == 2:
        return True

    # 3 - sqrt(num)
    for factor in range(3, int(math.sqrt(num)), 2):
        # not prime if num evenly divided by factor
        if num % factor == 0:
            return False

    return True


def compute():
    TARGET = fractions.Fraction(15499, 94744)
    totient = 1
    denominator = 1
    p = 2
    while True:
        totient *= p - 1
        denominator *= p
        # Note: At this point in the code, denominator is the product of one copy of each
        # prime number up to and including p, totient is equal to totient(denominator),
        # and totient/denominator = R'(2 * 3 * ... * p) (the pseudo-resilience).

        # Advance to the next prime
        while True:
            p += 1
            if eulerlib.is_prime(p):
                break

        # If the lower bound is below the target, there might be a suitable solution d such that
        # d's factorization only contains prime factors strictly below the current (advanced) value of p
        if fractions.Fraction(totient, denominator) < TARGET:
            # Try to find the lowest factor i such that R(i*d) < TARGET, if any.
            # Note that over this range of i, we have R'(d) = R'(i*d) < R(i*d).
            for i in range(1, p):
                numer = i * totient
                denom = i * denominator
                if fractions.Fraction(numer, denom - 1) < TARGET:
                    return str(denom)


print(compute())
