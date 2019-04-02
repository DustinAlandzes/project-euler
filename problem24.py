'''
A permutation is an ordered arrangement of objects.

If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from itertools import permutations

# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#assert 3124 in permutations([1, 2, 3, 4])

# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
#assert lexicographic_permutations([0, 1, 2]) == [012, 021, 102, 120, 201, 210]

print(''.join(map(str, [n for n in permutations(range(10))][10 ** 6 - 1])))