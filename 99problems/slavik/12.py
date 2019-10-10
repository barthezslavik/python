def decode(list):
    acc = []
    for item in list:
        number = item[0]
        value = item[1]
        final = []
        for x in range(0, number):
            final.append(value)
        acc.append(final)
    return acc

print(decode([[4, 1], [3, 2], [2, 3], [1, 1]]))
