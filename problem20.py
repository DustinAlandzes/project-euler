def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def sum_of_digits_in_factorial(number):
    # convert factorial to string, and then a list of strings
    list_of_chars = list(str(factorial(number)))
    # convert list of strings to list of ints
    list_of_ints = [int(x) for x in list_of_chars]
    # sum list of ints
    return sum(list_of_ints)


if __name__ == "__main__":
    # For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800
    assert factorial(10) == 3628800
    # and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    assert sum_of_digits_in_factorial(10) == 27
    """
    Find the sum of the digits in the number 100!
    """
    print(sum_of_digits_in_factorial(100))
