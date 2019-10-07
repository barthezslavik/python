def pack(list):
    result = [];
    for item in list:
        if len(result) == 0 or result[-1][0] != item:
            result.append(item) 
        #result[-1].append(item)
    return result

print(pack([1, 2, 2, 3, 3, 4, 5]))
