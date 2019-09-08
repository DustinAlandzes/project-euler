import itertools
import sys
import time


def pentagonal_numbers(n):
    """
    n(3n − 1) / 2

    :param n:
    :return:
    """
    return (n * (3 * n - 1)) // 2


if __name__ == "__main__":
    """
    Find the pair of pentagonal numbers, P_j and P_k
    
    for which their sum and difference are pentagonal and D = |P_k − P_j| is minimised
    
    what is the value of D?
    """
    start_time = time.time()
    integers = range(1, 3000)
    pentagonals = set(map(pentagonal_numbers, integers))

    minimum_difference = sys.maxsize
    for x, y in itertools.combinations(pentagonals, 2):
        sum_of_pair = x + y
        difference_of_pair = abs(x - y)
        # if sum and difference is pentagonal, and difference is smaller than minimum seen so far
        if sum_of_pair in pentagonals and difference_of_pair in pentagonals and minimum_difference > difference_of_pair:
            # this is the smallest difference (value of D)
            minimum_difference = difference_of_pair

    print(minimum_difference, time.time() - start_time)
