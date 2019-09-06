def fibonacci(n):
    if n <= 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
    assert fibonacci(11) == 89
    assert fibonacci(12) == 144

    """
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    """
    number = 1
    digits = 1
    prev = 1
    cur = 0

    while len(str(cur)) != 1000:
        number += 1
        # Advance the Fibonacci sequence by one step
        prev, cur = cur, prev + cur

    print(number, cur)
