import time

from problem07 import sieve_of_eratosthenes

if __name__ == "__main__":
    """
    The prime 41, can be written as the sum of six consecutive primes: 41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.
    
    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
    
    Which prime, below one-million, can be written as the sum of the most consecutive primes?
    """
    start_time = time.time()
    primes = sieve_of_eratosthenes(1000000)
    # length of the consecutive prime sum
    length = 0

    # value of the consecutive prime sum
    largest = 0

    # max value of the j variable(second for loop)
    lastj = len(primes)

    for i, prime in enumerate(primes):
        for j in range(i + length, lastj):
            # find sum of primes between i and j
            sol = sum(primes[i:j])
            if sol < 1000000:
                # if sum is prime
                if sol in primes:
                    length = j - i
                    largest = sol
            else:
                lastj = j + 1
                break
    print(largest, time.time() - start_time)
