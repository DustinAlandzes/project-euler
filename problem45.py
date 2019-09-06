'''
Find next number that is triangular, pentagonal and hexagonal
'''

def triangle_numbers(n):
    return (n * (n+1))/2


def pentagonal_numbers(n):
    return (n * (3*n-1)) / 2


def hexagonal_numbers(n):
    return n * (2*n-1)


integers = range(0, 1000)
triangles = list(map(triangle_numbers, integers))
pentagonals = list(map(pentagonal_numbers, integers))
hexagonals = list(map(hexagonal_numbers, integers))

# 40755 is triangular, pentagonal and hexagonal
assert triangles[285] == 40755
assert pentagonals[165] == 40755
assert hexagonals[143] == 40755

numbers = []
for x_index, x in triangles:
    for y_index, y in pentagonals:
        for z_index, z in hexagonals:
            if x == y and y == z:
                numbers.append((x_index, y_index, z_index))

print(numbers)
