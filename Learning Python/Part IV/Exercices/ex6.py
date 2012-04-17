def addDict(*dicts):
    result = {}
    for d in dicts:
        for k in d:
            result[k] = d[k]
    return result

if __name__ == '__main__':
    d1 = {1: 2, 3: 4, 'c': 'e'}
    d2 = {'a': 'b', 'c': 'd'}
    print(d1, d2, addDict(d1, d2))