from typing import List

def numbers_that_can_be_written_as_sum_of_nth_powers(n: int) -> List:
    """
    return list of numbers that can be written as the sum of of the nth power of their digits
    checks from 2 to 1000000
    """
    numbers = []
    # for every number until 1000000
    for x in range(2, 1000000):
        # if x == sum(each digit of x to the 5th power)
        if x == sum(int(d) ** n for d in str(x)):
            # add it to the list
            numbers.append(x)
    return numbers

assert numbers_that_can_be_written_as_sum_of_nth_powers(4) == [1634, 8208, 9474]
assert sum(numbers_that_can_be_written_as_sum_of_nth_powers(4)) == 19316

numbers = numbers_that_can_be_written_as_sum_of_nth_powers(5)
print(numbers)
print(sum(numbers))

