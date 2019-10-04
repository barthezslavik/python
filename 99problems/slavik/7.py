from nltk import flatten

def flat(list):
    return flatten(list)

print(flat([[1, 2, 3], [4, 5, [1, 2, 3]], [7], [8, 9]]))