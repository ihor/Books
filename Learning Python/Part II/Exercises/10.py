__author__ = 'Ihor Burlachenko'

record = {
    'name': {
        'first': 'Ihor',
        'last': 'Burlachenko'
    },
    'age': 24,
    'job': 'engineer',
    'address': {
        'city': 'Kyiv',
        'street': 'Kovalsky',
        'building': '22a',
        'apartment': '225'
    },
    'email': 'ihor.burlachenko@gmail.com',
    'phone': '+380502392179'
}

print(record['name'])
print(record['name']['first'])
print(record['job'])