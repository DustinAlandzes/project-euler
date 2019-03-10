'''
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def smallest_number_evenly_divisible_by_all_numbers_up_to(num):
    all_numbers = range(1, num)
    current_number = 1
    found = False

    while not found:
        for number in all_numbers:
            found = True
            if current_number % number != 0:
                found = False
                current_number += 1
                break

    return current_number

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
assert smallest_number_evenly_divisible_by_all_numbers_up_to(10) == 2520

print(smallest_number_evenly_divisible_by_all_numbers_up_to(20))
