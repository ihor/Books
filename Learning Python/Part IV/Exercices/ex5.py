def copyDict(d):
    result = {}
    for k in d:
        result[k] = d[k]
    return result

if __name__ == '__main__':
    d = {1: 2, 3: 4, 'a': 'b'}
    c = copyDict(d)
    d['c'] = 'd'
    print(d, c)