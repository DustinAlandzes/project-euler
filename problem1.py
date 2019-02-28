'''
Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_of_multiples(num):
    nums = []
    for x in range(num):
        if x % 3 == 0 or x % 5 == 0:
            nums.append(x)
    return sum(nums)

# If we list all the natural numbers below 10 that are multiples of 3 or 5
# we get 3, 5, 6 and 9. The sum of these multiples is 23.


assert sum_of_multiples(10) == 23

print(sum_of_multiples(1000))
