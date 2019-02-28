from functools import reduce
from itertools import combinations, combinations_with_replacement
'''
A palindromic number reads the same both ways.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(num):
    return str(num) == str(num)[::-1]

def generate_list_of_numbers(digits):
    return list(map(lambda x: int(''.join(x)), list(combinations_with_replacement(["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"], digits))))

def generate_pairs_of_numbers(number_list, terms):
    return list(combinations(number_list, terms))

def largest_palindrome(terms, digits):
    #import pdb; pdb.set_trace()
    numbers = generate_pairs_of_numbers(generate_list_of_numbers(digits), terms)
    for group in numbers:
        product = reduce((lambda x, y: x * y), group)
        if is_palindrome(product):
            return product
    raise Exception("Couldn't find a palindrome")

# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
assert largest_palindrome(2, 2) == 9009

print(largest_palindrome(2, 3))
