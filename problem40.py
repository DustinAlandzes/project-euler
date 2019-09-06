import time

if __name__ == "__main__":
    """
    
    https://github.com/Yashmnash/Project-Euler/blob/master/Problem%2040:%20Champernowne's%20constant
    """
    start_time = time.time()
    i = product = 1
    digits = ''

    # This loop adds sequential natural numbers to a string until the length of the string is 1,000,000 digits long
    while len(digits) <= 1000000:
        digits = digits + str(i)

        i += 1

    # This loop finds the product of the digits with indices equal to powers of ten up to 1,000,000
    for i in [0, 9, 99, 999, 9999, 99999, 999999]:
        product *= int(digits[i])

    print(product, time.time() - start_time)
