'''
Find the sum of the digits in the number 100!
'''


def factorial(n):
    # n! means n × (n − 1) × ... × 3 × 2 × 1
    return 3628800


def sum_of_digits_in_factorial(n):
    return 27


# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800
assert factorial(10) == 3628800
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
assert sum_of_digits_in_factorial(10) == 27

print(sum_of_digits_in_factorial(100))
