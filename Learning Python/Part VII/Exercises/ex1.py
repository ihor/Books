def oops():
    raise IndexError

def doomed():
    try:
        oops()
    except IndexError:
        print('Caught')

if __name__ == '__main__':
    doomed()