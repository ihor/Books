__author__ = 'Ihor Burlachenko'

# page 258, ...slicing always returns a new list object...
someList = []
someList[:3] = [1, 2, 3, 4]
print(someList)