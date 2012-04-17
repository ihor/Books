def countLines(fileObj):
    fileObj.seek(0)
    return len(fileObj.readlines())

def countChars(fileObj):
    fileObj.seek(0)
    return len(fileObj.read())

def test(fileName):
    fileObj = open(fileName)
    print('Lines: %d\nChars: %d' % (countLines(fileObj), countChars(fileObj)))

if __name__ == '__main__':
    import sys
    test(sys.argv[1])