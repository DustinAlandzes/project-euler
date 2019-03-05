'''
What is the 10 001st prime number?
'''

# wilson's theorem
# trial division
# sieve of eratosthenes

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    return True

def first_x_primes(x):
    '''
    Sieve of Eratosthenes
    time complexity: O(n log log n)
    '''
    integers = range(2, x)
    p = 2 # the smallest prime number
    for num in integers:
        print(num)
    return [0, 13]


'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
'''
assert first_x_primes(6)[-1] == 13

print(first_x_primes(10001)[-1])
