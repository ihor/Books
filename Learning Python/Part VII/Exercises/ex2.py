class MyError(Exception): ...

def oops():
    raise MyError

def doomed():
    try:
        oops()
    except (IndexError, MyError):
        print('Caught')

if __name__ == '__main__':
    doomed()