def divisors(n):
    """
    takes integer n

    returns list of integers
    who evenly divide by n
    """
    proper_divisors = []
    for x in range(1, n // 2 + 1):
        if not (n % x):
            proper_divisors.append(x)
    return proper_divisors


def abundant_numbers():
    """
    By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
    """
    abundant_numbers = []
    for n in range(28123, 1, -1):
        if sum(divisors(n)) > n:
            abundant_numbers.append(n)
    print("generated abundant numbers")
    return abundant_numbers


def sums_of_abundant_numbers():
    sums = set()
    abundant = abundant_numbers()
    for x in abundant:
        for y in abundant:
            if (x + y) < 28123:
                sums.add(x + y)
    print("generated sums of abundant numbers")
    return sums


def sum_of_non_abundant_numbers():
    sums = sums_of_abundant_numbers()
    result = 0
    for n in range(28123):
        if n not in sums:
            result += n
    return result


if __name__ == "__main__":
    # O(n^5)
    """
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    """
    print(sum_of_non_abundant_numbers())
