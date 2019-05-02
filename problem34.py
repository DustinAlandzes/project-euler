'''
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
'''


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


def sum_of_factorial_of_digits(number):
    digits = []
    for digit in str(number):
        digits.append(int(digit))
    factorial_of_digits = map(factorial, digits)
    return sum(factorial_of_digits)


assert(sum_of_factorial_of_digits(145) == 145)

numbers = set()
for x in range(100000):
    if sum_of_factorial_of_digits(x) == x:
        numbers.add(x)
print(sum(numbers))

'''
total = 0
factorials = {}
for i in xrange(10):
    factorials[str(i)] = math.factorial(i)
for i in xrange(3, 50000):
    factorial_sum = 0
    for j in str(i):
        factorial_sum += factorials[j]
    if factorial_sum == i:
        total += factorial_sum
return total
'''
