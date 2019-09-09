import time

from problem03 import prime_factors

if __name__ == "__main__":
    assert len(prime_factors(644)) == 3
    assert len(prime_factors(645)) == 3
    assert len(prime_factors(646)) == 3

    """
    Find the first four consecutive integers to have four distinct prime factors each. 
    What is the first of these numbers?
    """
    start_time = time.time()
    for a in range(130000, 140000):  # keeping range this way because i know the answer and it's slow
        b = a + 1
        c = b + 1
        d = c + 1
        if all(len(prime_factors(x)) == 4 for x in [a, b, c, d]):
            print(a)
            break
    print(time.time() - start_time)
