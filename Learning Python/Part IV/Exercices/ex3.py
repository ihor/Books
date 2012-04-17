def adder(*pargs, **kargs):
    if pargs:
        result = pargs[0]
    elif kargs:
        key, result = kargs.popitem()
    else:
        raise TypeError('adder() needs at least 1 argument (0 given)')

    for arg in pargs[1:]:
        result += arg
        
    for arg in kargs:
        result += kargs[arg]

    return result

if __name__ == '__main__':
    print('adder(1, 2, 3, a = 4) = ', adder(1, 2, 3, a = 4))
    print('adder(1.0, 2, a = 3.1, b = 3.9) = ', adder(1.0, 2, a = 3.1, b = 3.9))
    print("adder('sp', 'am', a = 'eggs') = ", adder('sp', 'am', a = 'eggs'))
    print("adder(['s', 'p'], ['a', 'm'], a = ['e', 'g'], b = ['g', 's']) = ", adder(['s', 'p'], ['a', 'm'], a = ['e', 'g'], b = ['g', 's']))    