import time

from problem04 import is_palindrome


def is_palindromic_in_base10_and_base2(number):
    if is_palindrome(number) and is_palindrome(bin(number)[2:]):
        return True
    return False


def sum_of_palindromic_numbers_under_1_million():
    palindromes = []
    for x in range(1000000):
        if is_palindromic_in_base10_and_base2(x):
            palindromes.append(x)
    return sum(palindromes)


if __name__ == "__main__":
    """
    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    """
    time1 = time.time()
    print(sum_of_palindromic_numbers_under_1_million())
    print(f"finished in {time.time() - time1}")
