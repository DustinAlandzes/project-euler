import itertools
import time

from problem07 import sieve_of_eratosthenes


def substring_divisible(x):
    """
    Determine if number is substring divisible

    check that each 3 digit part is divisible by all the primes up to 18
    :param x:
    :return:
    """
    # iterate through successive three digits and check if they
    # can be divided by successively larger primes
    for i, j in zip(sieve_of_eratosthenes(18), range(1, 8)):
        if int(x[j:j + 3]) % i == 0:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    """
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
    but it also has a rather interesting sub-string divisibility property.
    
    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d_2 * d_3 * d_4 = 406 is divisible by 2
    d_3 * d_4 * d_5 = 063 is divisible by 3
    d_4 * d_5 * d_6 = 635 is divisible by 5
    d_5 * d_6 * d_7 = 357 is divisible by 7
    d_6 * d_7 * d_8 = 572 is divisible by 11
    d_7 * d_8 * d_9 = 728 is divisible by 13
    d_8 * d_9 * d_10 = 289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    """
    start = time.time()
    # pandigital numbers that don't start with 0
    pandigital_numbers = [''.join(x) for x in itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
                          if (x[0] != '0')]

    # answer is the sum of all pandigitals that are substring divisible
    answer = sum([int(number) for number in pandigital_numbers if substring_divisible(number)])
    print(f'The answer is {answer}, found in {time.time() - start} seconds')
