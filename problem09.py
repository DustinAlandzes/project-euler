from itertools import combinations_with_replacement
from functools import reduce
from operator import add, mul

'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def is_pythagorean_triplet(triplet):
    '''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2
    '''
    # if a < b < c
    if not ((triplet[0] < triplet[1]) and (triplet[1] < triplet[2])):
        return False
    # and a^2 + b^2 = c^2
    if not ((triplet[0]**2 + triplet[1]**2) == triplet[2]**2):
        return False
    # it's a pythagorean triplet
    return True


def pythagorean_triplets():
    '''
    A generator that filters a list of all triplets
    and yields the pythagorean triplets
    '''
    # generate all triplets from 0, 0, 0 to 9, 9, 9
    # list of tuples: [(0, 0, 0), (0, 0, 1), ..., (9, 9, 9)]
    triplets = combinations_with_replacement(range(1, 1000), 3)

    # filter for triplets
    for triplet in triplets:
        # if a < b < c and a^2 + b^2 = c^2
        if is_pythagorean_triplet(triplet):
            yield triplet


# find pythagorean triplet with the sum of 1000
# and find the product
for triplet in pythagorean_triplets():
    if reduce(add, triplet) == 1000:
        print(triplet)
        print(reduce(add, triplet))
        print(reduce(mul, triplet))
        break
