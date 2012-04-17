from operator import mul

def sqrFor(l):
    result = []
    for i in l:
        result.append(i * i)
    return result

def sqrMap(l):
    return map(mul, l, l)

def sqrGen(l):
    return [i * i for i in l]

if __name__ == '__main__':
    l = [2, 4, 9, 16, 25]
    print(sqrFor(l))
    print(list(sqrMap(l)))
    print(sqrGen(l))
