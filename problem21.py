from tools import measure_execution_time


def divisors(n):
    '''
    takes integer n

    returns list of integers
    who evenly divide by n
    '''
    proper_divisors = []
    for x in range(1, n // 2 + 1):
        if not (n % x):
            proper_divisors.append(x)

    return proper_divisors


def d(n):
    '''
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    '''
    return sum(divisors(n))


@measure_execution_time
def amicable_numbers_up_to(n):
    '''
    If d(a) = b and d(b) = a, where a != b,
    then a and b are an amicable pair and each of a and b are called amicable numbers.
    '''
    amicable_numbers = set()

    for a in range(1, n):
        d_a = d(a)
        d_b = d(d_a)

        if a == d_b and d_a != d_b:
            amicable_numbers.add(d_a)

    return amicable_numbers


if __name__ == "__main__":
    assert divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    assert d(220) == 284

    assert divisors(284) == [1, 2, 4, 71, 142]
    assert d(284) == 220

    print(amicable_numbers_up_to(10000))
    """
    Evaluate the sum of all the amicable numbers under 10000.
    """
    print(sum(amicable_numbers_up_to(10000)))
