"""
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""
n0 = 1
n1 = 2
L = 100

# 2 - 101
for i in range(2, L+1):
    n0 = n1
    if i % 3:
        n1 = n0 + n1 * 1
    else:
        n1 = n0 + n1 * (2 * i//3)

print(sum(map(int, str(n1))))
