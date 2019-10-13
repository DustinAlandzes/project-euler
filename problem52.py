import time
from collections import Counter

if __name__ == "__main__":
    # Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    start_time = time.time()
    x = 1
    while True:
        variants = [x * y for y in range(2, 7)]  # x * 2, x * 3, ..., x * 6
        if all(not (Counter(str(x)) - Counter(str(y))) for y in variants):  # compares count of each digit
            print(x, variants, time.time() - start_time)
            break
        x += 1
