'''
Evaluate the sum of all the amicable numbers under 10000.
'''

def divisors(n):
    return 1

def d(n):
    '''
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    '''
    return sum(divisors(n))


def amicable_numbers():
    '''
    If d(a) = b and d(b) = a, where a ≠ b,
    then a and b are an amicable pair and each of a and b are called amicable numbers.
    '''
    return 1

assert divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55]
assert d(220) = 284

assert divisors(284) == [1, 2, 4, 71, 142]
assert d(284) == 220
