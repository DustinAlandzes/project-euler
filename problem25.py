'''
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
#RecursionError: maximum recursion depth exceeded in comparison
def fibonacci(n):
    if n <= 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

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

number = 100000
digits = 1
while digits != 1000:
    print(fibonacci(number))
    digits == len(str(fibonacci(number)))
    number += 1
