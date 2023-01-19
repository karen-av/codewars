import itertools

strng = 'abcc'
res = []
a = itertools.permutations(strng)
for i in a:
    m = ''.join(i)
    res.append(m)
print(res)

repeat = set(x for x in res if res.count(x) > 1)
print(f'repeat - {repeat}')