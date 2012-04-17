def adder(a, b):
    return a + b

if __name__ == '__main__':
    print('adder(1, 2) = ', adder(1, 2))
    print('adder(1.0, 2) = ', adder(1.0, 2))
    print("adder('sp', 'am') = ", adder('sp', 'am'))
    print("adder(['s', 'p'], ['a', 'm']) = ", adder(['s', 'p'], ['a', 'm']))