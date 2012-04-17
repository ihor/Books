class MyList(list):
    def __add__(self, value):
        print('Custom add')
        return list.__add__(self, value)

    def __getitem__(self, index):
        print('Custom getitem')
        return list.__getitem__(self, index)

if __name__ == '__main__':
    myList = MyList((1, 2, 3))
    print(myList + [4, 5, 6])
    print(myList[2])
    print(myList[0:2])