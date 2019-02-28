'''
What is the largest prime factor of the number 600851475143 ?
'''


def prime_factors(num):
    d = 2
    factors = []
    while num > 1:
        if num % d == 0:
            factors.append(d)
            num = num / d
        else:
            d = d + 1
    return factors

# the prime factors of 13195 are 5, 7, 13 and 29.


assert(prime_factors(13195) == [5, 7, 13, 29])
print(prime_factors(600851475143))
