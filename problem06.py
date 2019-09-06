import time


def sum_of_squares(numbers):
    squares = map(lambda x: x**2, numbers)
    return sum(squares)


def square_of_sum(numbers):
    total = sum(numbers)
    return total**2


if __name__ == "__main__":
    assert sum_of_squares(range(1, 11)) == 385
    assert square_of_sum(range(1, 11)) == 3025
    assert (square_of_sum(range(1, 11)) - sum_of_squares(range(1, 11))) == 2640

    """
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    start_time = time.time()
    print(square_of_sum(range(1, 101)) - sum_of_squares(range(1, 101)), time.time() - start_time)
