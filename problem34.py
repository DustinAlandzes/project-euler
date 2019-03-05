'''
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
'''


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


def sum_of_factorial_of_digits(number):
    digits = []
    for digit in str(number):
        digits.append(int(digit))
    factorial_of_digits = map(factorial, digits)
    return sum(factorial_of_digits)


assert(sum_of_factorial_of_digits(145) == 145)
