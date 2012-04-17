def getFactorOf(number):
    for i in range(2, int(number // 2)):
        if number % i == 0:
            return i

    return None

def check(number):
    factor = getFactorOf(number)
    if factor:
        print(number, 'has factor', factor)
    else:
        print(number, 'is prime')

if __name__ == '__main__':
    check(13)
    check(13.0)
    check(15)
    check(15.0)