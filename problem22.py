'''
load p022_names.txt a 46K text file containing over five-thousand first names
sort it into alphabetical order
get name score of each name
sum score of each name
'''


def load_file():
    '''
    loads and processes p022_names.txt
    '''
    text_file = open("p022_names.txt", "r")
    # read file, remove double quotes, split into list by comma, sort alphabetically
    names = sorted(text_file.read().replace('\"', "").split(','))
    return names


def position_on_list(str, list_of_names):
    '''
    given a string and list of strings
    returns position of string in the list
    '''
    for i, name in enumerate(list_of_names):
        if str == name:
            return i+1
    return False


def alphabetal_position(letter):
    '''
    returns alphabetical position of character
    '''
    return ord(letter) - 64


def alphabetical_value(name):
    '''
    given a string
    returns the sum of the alphebetical position of each character
    '''
    value = 0
    for letter in name:
        value += alphabetal_position(letter)
    return value


def name_score(name, list_of_names):
    '''
    given a string and list of strings
    returns product of string's position on the list, and "alphabetical value" of the string
    '''
    return position_on_list(name, list_of_names) * alphabetical_value(name)


def get_sum_of_all_scores(list_of_names):
    scores = []

    # for every name in the list, generate a score
    for name in list_of_names:
        scores.append(name_score(name, list_of_names))

    # add all the scores together
    return sum(scores)


names = load_file()
assert name_score("COLIN", names) == 49714
print(get_sum_of_all_scores(names))
