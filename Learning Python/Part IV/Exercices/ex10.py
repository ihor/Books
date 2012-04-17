import math, mytimer, sys
reps = 1000
repslist = range(reps);

def sqrtMathSqrt():
    for i in repslist:
        math.sqrt(i)

def sqrtExp():
    for i in repslist:
        i ** .5

def sqrtPow():
    for i in repslist:
        pow(i, .5)

if __name__ == '__main__':
    print(sys.version)
    for tester in (mytimer.timer, mytimer.best):
        print()
        print(tester.__name__)
        for test in (sqrtMathSqrt, sqrtExp, sqrtPow):
            time = tester(test, _reps = reps)
            print('-' * 35)
            print('%-9s: %.5f' % (test.__name__, time))
        print('-' * 35)
