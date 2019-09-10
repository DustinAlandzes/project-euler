import itertools

from problem07 import sieve_of_eratosthenes

if __name__ == "__main__":
    """
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
    
    https://radiusofcircle.blogspot.com/2016/06/problem-49-project-euler-solution-with-python.html
    """
    # 4 digit primes
    primes = [prime for prime in sieve_of_eratosthenes(10000) if len(list(str(prime))) == 4 and prime > 1487]
    for key, prime in enumerate(primes):
        # get list of permutations, and convert to ints (permutations() returns list of strings)
        permutation_numbers = [int(''.join(x)) for x in itertools.permutations(str(prime)) if int(''.join(x)) in primes]
        # get rid of non prime permutations
        permutation_numbers = list(set([number for number in permutation_numbers if number in primes]))

        # check that they all of the same difference?
        for i in range(len(permutation_numbers)):
            for j in range(i + 1, len(permutation_numbers)):
                difference = permutation_numbers[j] - permutation_numbers[i]
                if permutation_numbers[j] + difference in permutation_numbers:
                    print(str(permutation_numbers[i]) + str(permutation_numbers[j]) + str(
                        permutation_numbers[j] + difference))
                    exit()
