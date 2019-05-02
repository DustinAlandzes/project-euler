"""
find the minimal path sum
from the top left to the bottom right
by only moving right and down
"""
from itertools import accumulate

import requests


def minimal_path_sum(matrix):
    # accumulate sum for top row
    # accumulate sum for left column
    # for each i,j pair
    #   add min of left cell and upper cell
    #   the result is stored in the last i,j pair
    rows = iter(matrix)
    best = list(accumulate(next(rows)))
    if not best:
        return 0  # 0 columns

    for row in rows:
        best[0] += row[0]
        for j in range(1, len(row)):
            best[j] = row[j] + min(best[j - 1],  # approaching from the left
                                   best[j])  # approaching from above
    return best[-1]


test_grid = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [530, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

assert minimal_path_sum(test_grid) == 2427

response = requests.get("https://projecteuler.net/project/resources/p081_matrix.txt")
real_grid = []
for line in response.text.strip().split("\n"):
    real_grid.append(list(map(int, line.strip().split(","))))

print(real_grid)
print(minimal_path_sum(real_grid))
