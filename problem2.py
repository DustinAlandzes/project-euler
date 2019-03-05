'''
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''


def fibonacci(steps, limit=4000000):
    '''
    Each new term in the Fibonacci sequence is generated by adding the previous two terms
    '''
    sequence = [1, 2]
    for x in range(steps - 2):
        # if the sum of last two is greater than specified limit, stop
        if (sequence[-1] + sequence[-2]) > limit:
            break
        # otherwise, add the term to the sequence
        else:
            sequence.append(sequence[-1] + sequence[-2])
    return sequence


# by starting with 1 and 2, the first 10 terms will be 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
assert fibonacci(10, limit=10) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

sum_of_evens = sum([i for i in fibonacci(1000) if i % 2 == 0])
print(sum_of_evens)
