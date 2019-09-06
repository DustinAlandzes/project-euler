from functools import wraps
from time import time


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
