'''
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
how many routes are there through a 20×20 grid?
'''

# todo iterative and recursive solutions
# https://projecteuler.net/overview=015


def routes_through_grid(n):
    # i guess this is the combinatorial solution
    # https://codereview.stackexchange.com/a/128838

    # start at 1
    ret = 1

    # for every number from 1 to n+1
    for j in range(1, n+1):
        # multiply by number + grid size
        ret *= n + j
        # divide by grid size
        ret //= j
    return ret


assert routes_through_grid(2) == 6

print(routes_through_grid(20))
