class Adder:
    def __init__(self, data):
        self.data = data

    def add(self, x, y):
        print('Not implemented')
        
    def __add__(self, value):
        return self.add(self.data, value)

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        res = {}
        for d in (x, y):
            for k in d:
               res[k] = d[k]
        return res

if __name__ == '__main__':
    listAdder = ListAdder([1, 2])
    dictAdder = DictAdder({5:6})
    print(listAdder.add([1], [2]))
    print(listAdder + [3])
    print(dictAdder.add({1:2}, {3:4}))
    print(dictAdder + {7:8})