from timeit import timeit
"""
There are eight coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)

How many different ways can £2 be made using any number of coins?

https://www.algorithmist.com/index.php/Coin_Change:

given an integer N and a set of integers S = {S_1, S_2, ..., S_m}
how many ways can one express N as a linear combination of S with non-negative coefficients

how many solutions are there to N = sum{k=1..m}{x_k S_k}, where x_k >= 0, and k is an integer from 1 to m

if N = 4 and S = {1, 2, 3}
there are four solutions: {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1,3}

if N = 200 and S = {1, 2, 5, 10, 20, 50, 100, 200}
there are ? solutions: {1} * 200, {200}, {2} * 100, {100, 100}, {100, 50, 50}, {50, 50, 50, 50} ...

we are trying to count the number of distinct sets.
the set of solutions for this problem, C(N, m), can be partitioned into two sets:

1. there are those sets that do not contain any S_m
2. those sets that contain at least 2 S_m

if a solution does not contain S_m, then we can solve the subproblem of N with S = {S_1, S_2, ..., S_m-1},
or the solutions of C(N, m - 1)

if a solution does contain S_m, then we are using at least one S_m, 
thus we are now solving the sub problem of N - S_m, S = {S_1, S_2, ..., S_m}
This is C(N - S_m, m)

thus we can formulate the following:
C(N, m) = C(N, m - 1) + C(N - S_m, m)
with the base cases:
 * C(N, m) = 1, N = 0 (one solution, 0)
 * C(N, m) = 0, N < 0 (no solution, negative)
 * C(N, m) = 0, N >= 1, m <= 0 (no solution, no coins)
"""

coins_in_circulation = [1, 2, 5, 10, 20, 50, 100, 200]

def brute_force(n=200):
    ways = dict()
    # start at 1
    ways[0] = 1
    # for every coin
    for coin in coins_in_circulation:
        # for every integer from coin to n + 1
        for pence_left in range(coin, n+1):
            # start at 0
            if pence_left not in ways:
                ways[pence_left] = 0
            # ways for this are the sum of the ways for
            ways[pence_left] += ways[pence_left - coin]
    return ways[200]

# todo recursive, dp

if __name__ == "__main__":
    print(brute_force(200))
