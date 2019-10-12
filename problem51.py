import time
from collections import Counter
from typing import List

from problem07 import sieve_of_eratosthenes


# https://blog.dreamshire.com/project-euler-51-solution/
# https://radiusofcircle.blogspot.com/2016/06/problem-51-project-euler-solution-with-python.html

def families(prime: int) -> List[List[str]]:
    """
    generates lists of prime with duplicates replaced

    families(566003) returns
    [[566003,566113,566223,566333,566443,566553,566663,566773,566883,566993],
    [500003,511003,522003,533003,544003,555003,566003,577003,588003,599003]]

    :param prime: number
    :return: list
    """
    prime = str(prime)
    families = []
    # for every number repeated more than once
    for duplicate in (Counter(prime) - Counter(set(prime))):
        # replace that number with every other number
        families.append([prime.replace(duplicate, number) for number in '0123456789'])
    return families


def is_the_one_we_want(prime: int, primes: List[int]) -> bool:
    """
    checks if by replacing all of one digit this prime generates a family of 8 primes

    :param prime: prime we're replacing the digits of
    :param primes: list of primes to compare against
    :return:
    """
    for family in families(prime):
        if len([number for number in family if number in primes]) == 8:  # if all eight replacements are prime
            return True
    return False


if __name__ == "__main__":
    start_time = time.time()
    primes = sieve_of_eratosthenes(1000000)
    primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]  # only primes that have 3 repeating digits
    for prime in primes:
        if is_the_one_we_want(prime, primes):
            print(prime)
            break
    print(time.time() - start_time)
