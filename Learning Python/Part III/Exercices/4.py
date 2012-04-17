l = [1, 2, 4, 8, 16, 32, 64]
x = 5


# Original code

found = False
i = 0
while not found and i < len(l):
    if 2 ** x == l[i]:
        found = 1
    else:
        i = i + 1

if found:
    print('At index', i)
else:
    print(x, 'not found')


# Refactored code

if 2 ** x in l:
    print('At index', l.index(2 ** x))
else:
    print(x, 'not found')
