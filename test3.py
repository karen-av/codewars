import itertools

strng = 'aabb'
res = []
a = itertools.permutations(strng)
for i in set(a):
    m = ''.join(i)
    print(f'i - {i}\nm - {m}')
    print(type(m))
    res.append(m)
print(res)

x = ('a', 'b', 'c')
c = '#'.join(x)
print(c)

def permutations(x):
    return list(''.join(i) for i in set(itertools.permutations(x)))

strng = 'aabb'
done = permutations(strng)
print(done)