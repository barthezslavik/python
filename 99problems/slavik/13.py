def encodeDirect(list):
    changes = []
    for index, item in enumerate(list):
        if index != 0:
            if item != list[index - 1]:
                changes.append(index)
    changes.append(len(list))
    length = len(changes)

    result = []
    for i in range(0, length):
        #count = changes[i] - changes[i - 1]
        #value = list[changes[i]]
        #if i == 0:
        #result.append([1, value])
        #else:
        #    result.append([count, value])
    return result

print(encodeDirect([4, 1, 1, 3, 3, 2, 2, 3, 1, 1]))


