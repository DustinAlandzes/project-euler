def sum_of_self_power(numbers):
    return sum(map(lambda x: x**x, numbers))

assert sum_of_self_power(range(1, 11)) == 10405071317

print(str(sum_of_self_power(range(1, 1001)))[-10:])
