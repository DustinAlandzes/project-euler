"""
https://radiusofcircle.blogspot.com/2016/05/problem-38-project-euler-solution-with-python.html
"""
import time


def find_largest_pandigital():
    largest = 0
    # for loop to loop till 4 digits
    for i in range(1, 10000):
        # value for concatenated product
        multiplication = ''

        # (1,2,3,4,.....n)
        integer = 1

        # if the multiplication < 9 digits
        while len(multiplication) < 9:
            # concatenating the product at each stage
            multiplication += str(i * integer)
            # incrementing (1,2,3,4,....n)
            integer += 1

        # check for digits less than 9
        # check for all 1-9 numbers
        # check if '0' not in concatenated sting
        if ((len(multiplication) == 9) and (len(set(multiplication)) == 9)
            and ('0' not in multiplication)) and int(multiplication) > largest:
            largest = int(multiplication)

    return largest


if __name__ == "__main__":
    time1 = time.time()
    print(find_largest_pandigital(), time.time() - time1)
