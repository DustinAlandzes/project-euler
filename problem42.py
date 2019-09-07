def triangle_numbers(n):
    """
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1)
    """
    return (n * (n + 1)) // 2


triangle_numbers_list = [triangle_numbers(n) for n in range(1, 10000)]


def is_triangle_word(word):
    letter_values = []
    for letter in word:
        letter_values.append(ord(letter) - 64)
    return sum(letter_values) in triangle_numbers_list


if __name__ == "__main__":
    """
    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
    """
    assert [triangle_numbers(x) for x in range(1, 11)] == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert is_triangle_word("SKY")
    with open("p042_words.txt") as f:
        words = f.read().replace('\"', '').split(',')

    triangle_words = []
    for word in words:
        if is_triangle_word(word):
            triangle_words.append(word)
    print(len(triangle_words), triangle_words)
