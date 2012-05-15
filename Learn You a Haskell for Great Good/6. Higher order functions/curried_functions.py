import inspect

def partial(f, *ppargs, **pkargs):
    return lambda *pargs, **kargs: f(*(ppargs + pargs), **dict(pkargs, **kargs))

def curried(f, *cpargs, **ckargs):
    argspec = inspect.getargspec(f)
    assert argspec[1] == None, "Can't curry function with *pargs"
    assert argspec[2] == None, "Can't curry function with **kargs"
    assert argspec[3] == None, "Can't curry function with default arguments"

    if (len(cpargs) + len(ckargs)) >= f.__code__.co_argcount:
        return f(*cpargs, **ckargs)

    return lambda *pargs, **kargs: curried(f, *(cpargs + pargs), **dict(ckargs, **kargs))

if __name__ == '__main__':
    def add(x, y):
        return x + y

    inc = partial(add, 1)
    assert inc(2) == 3

    dec = partial(add, -1)
    assert dec(2) == 1

    reverse = partial(sorted, reverse=True)
    assert reverse([1, 2, 3]) == [3, 2, 1]

    def calc(x, y, z):
        return x + 2*y + 3*z

    curried_calc = curried(calc)
    assert curried_calc(1)(2)(3) == calc(1, 2, 3)
    assert curried_calc(z=1)(2)(3) == calc(2, 3, 1)
    assert curried_calc(z=1)(y=2)(3) == calc(3, 2, 1)
