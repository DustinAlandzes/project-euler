def sum_of_self_power(numbers):
    return sum(map(lambda x: x**x, numbers))


if __name__ == "__main__":
    assert sum_of_self_power(range(1, 11)) == 10405071317
    """
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """
    print(str(sum_of_self_power(range(1, 1001)))[-10:])
