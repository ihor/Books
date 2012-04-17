s = 'abcdefghjiklmnopqrstuvxyz'

# a
for char in s:
    print(ord(char))

# b
codesSum = 0
for char in s:
    codesSum += ord(char)

print('The sum is: {0}'.format(codesSum))

# c
charCodes = []
for char in s:
    charCodes.append(ord(char))

print('Char codes are: {0}'.format(charCodes))

# c1
print('Char codes are: {0}'.format(list(map(ord, s))))