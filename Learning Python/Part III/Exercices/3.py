s = 'abcdefghjiklmnopqrstuvxyz'

d = dict(zip(map(ord, s), s))
for k in sorted(d):
    print('{0} => {1}'.format(k, d[k]))
