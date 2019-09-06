import time

from problem20 import factorial


def sum_of_factorial_of_digits(number):
    digits = []
    for digit in str(number):
        digits.append(int(digit))
    factorial_of_digits = map(factorial, digits)
    return sum(factorial_of_digits)


if __name__ == "__main__":
    assert (sum_of_factorial_of_digits(145) == 145)

    """
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    """
    start_time = time.time()
    numbers = set()
    for x in range(100000):
        if sum_of_factorial_of_digits(x) == x:
            numbers.add(x)
    print(sum(numbers), time.time() - start_time)
