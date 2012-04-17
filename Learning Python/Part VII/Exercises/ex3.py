from sys import exc_info
from traceback import print_exc

def oops():
    raise IndexError

def safe(func, *args):
    try:
        func(*args)
    except:
        print('Caught exception', exc_info()[0])
        print_exc()

if __name__ == '__main__':
    safe(oops)