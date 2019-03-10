from itertools import count


def collatz_squence():
    for index in count(1):
        if index % 2 == 0:
            # even
            yield index / 2
        # odd
        yield (3 * index) + 1
