from problem42 import triangle_numbers

def pentagonal_numbers(n):
    return (n * (3 * n - 1)) // 2


def hexagonal_numbers(n):
    return n * (2*n-1)


if __name__ == "__main__":
    integers = range(0, 100000)
    triangles = list(map(triangle_numbers, integers))
    pentagonals = list(map(pentagonal_numbers, integers))
    hexagonals = list(map(hexagonal_numbers, integers))

    # 40755 is triangular, pentagonal and hexagonal
    assert triangles[285] == 40755
    assert pentagonals[165] == 40755
    assert hexagonals[143] == 40755

    """
    Find next number after 40755 that is triangular, pentagonal and hexagonal
    """

    print(set(triangles) & set(pentagonals) & set(hexagonals))
