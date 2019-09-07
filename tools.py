from functools import wraps
from time import time

from problem20 import factorial


def measure_execution_time(f):
    """
    decorator that prints the execution time of a function
    originally from https://codereview.stackexchange.com/a/169876
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f"Execution time: {end - start}")
        return result

    return wrapper


def combinations(list_of_items):
    """

    nPr = n! / (n_1! * n_2! * ... * n_k!)
    nPr(['s','t','a','t','i','s','t','i','c','s']) ==  50400
    :param list_of_items:
    :return: number of different combinations
    """
    numerator = factorial(len(list_of_items))  # n!
    char_counts = {}
    for item in list_of_items:
        char_counts[item] = list_of_items.count(item)
    denominator = 1
    for count in char_counts:
        denominator *= factorial(char_counts[count])  # n_1! * n_2! * ... * n_k!
    return numerator // denominator
