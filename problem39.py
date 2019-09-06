"""
If p is the **perimeter of a right angle triangle with integral length sides** {a,b,c}

there are exactly three solutions for p = 120:
{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

a^2 + b^2 = c^2
where
c - length of hypotenuse
a, b - length of two other sides

a + b + c = p
where
p - perimeter
"""
import time


def solutions_for(p):
    """
    a + b + c = p
    c = p - a - b

    a^2 + b^2 = c^2
    :param p:
    :return:
    """
    solutions = []
    for a in range(1, int(p / 3)):
        for b in range(500):
            # find c
            c = p - a - b
            # see if this equation satisfied our constraints
            if (a + b + c) == p and (a ** 2 + b ** 2) == c ** 2:
                # if so add to list
                solutions.append({'a': a, 'b': b, 'c': c, 'p': p})
    return solutions


def max_solutions_for_p_below(n):
    max_solutions = []
    for p in range(1, n):
        solutions_for_p = solutions_for(p)
        if len(solutions_for_p) > len(max_solutions):
            max_solutions = solutions_for_p
    print(max_solutions)
    return len(max_solutions)


assert solutions_for(120) == [{'a': 20, 'b': 48, 'c': 52, 'p': 120}, {'a': 24, 'b': 45, 'c': 51, 'p': 120},
                              {'a': 30, 'b': 40, 'c': 50, 'p': 120}]
assert len(solutions_for(120)) == 3

if __name__ == "__main__":
    start_time = time.time()
    print(max_solutions_for_p_below(1000), time.time() - start_time)
