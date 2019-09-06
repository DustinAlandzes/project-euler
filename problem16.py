def sum_of_digits(number):
    digits = []
    for digit in str(number):
        digits.append(int(digit))
    return sum(digits)


if __name__ == "__main__":
    assert 2 ** 15 == 32768
    assert sum_of_digits(2 ** 15) == 26
    """
    What is the sum of the digits of the number 2^1000?
    """
    print(sum_of_digits(2 ** 1000))
