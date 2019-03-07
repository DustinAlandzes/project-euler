from itertools import combinations_with_replacement
from functools import reduce
from operator import add, mul

'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def pythagorean_triplets():
    '''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2
    '''
    # generate all triplets from 0, 0, 0 to 9, 9, 9
    # list of tuples: [(0, 0, 0), (0, 0, 1), ..., (9, 9, 9)]
    triplets = combinations_with_replacement(range(1, 1000), 3)

    # filter for triplets where 0 < 1 < 2
    for triplet in triplets:
        # if a < b < c and a^2 + b^2 = c^2
        if ((triplet[0] < triplet[1]) and (triplet[1] < triplet[2])) and ((triplet[0]**2 + triplet[1]**2) == triplet[2]**2):
            yield triplet


for triplet in pythagorean_triplets():
    print(triplet)
    if reduce(add, triplet) == 1000:
        print(triplet)
        print(reduce(add, triplet))
        print(reduce(mul, triplet))
        break

# 32 + 42 = 9 + 16 = 25 = 52.
