def pack(list):
    result = []

    for index, item in enumerate(list):
        if index == 0 or item != list[index-1]:
            result.append([item])
        else:
            result[-1].append(item)
    return result

def encode(list):
    acc = []
    for item in list:
        element = [len(item), item[0]]
        acc.append(element)
    return acc 

print(encode(pack([1, 2, 2, 3, 3, 4, 5, 5, 2, 2, 1])))
