"""
digit cancelling fractions

49/98 = 4/8
30/50 = 3/5

find four non-trivial examples of this type of fraction
less than one in value
containing two digits in the numerator and denominator

http://mathworld.wolfram.com/AnomalousCancellation.html

"""
import time
from fractions import Fraction


def remove_common_digits(numerator, denominator):
    # Intersection of Two sets(Common number between the two)
    common = list(set(str(numerator)).intersection(set(str(denominator))))
    # Check if the list is not empty
    if len(common) != 0 and common[0] != '0':
            num = list(str(numerator))
            den = list(str(denominator))
            # Remove the common element from numerator
            num.remove(common[0])
            # Remove the common element from Denominator
            den.remove(common[0])
            if num[0] != '0' and den[0] != '0':
                return int(num[0]), int(den[0])
    return None, None


def get_digit_canceling_fractions():
    fractions = []
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            original_fraction = Fraction(numerator, denominator)
            reduced_numerator, reduced_denominator = remove_common_digits(numerator, denominator)
            if not reduced_numerator or not reduced_denominator:
                continue
            reduced_fraction = Fraction(reduced_numerator, reduced_denominator)
            if original_fraction == reduced_fraction:
                fractions.append(original_fraction)
    return fractions


if __name__ == "__main__":
    # get product of fractions
    start_time = time.time()
    product = 1
    fractions = get_digit_canceling_fractions()
    for fraction in fractions:
        product *= fraction
    print(product.denominator, product, fractions)
    print(time.time() - start_time)
