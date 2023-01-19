"""
DESCRIPTION:

In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
Note: The order of the permutations doesn't matter.

Good luck!

"""


import itertools
#https://docs-python.ru/standart-library/modul-itertools-python/funktsija-permutations-modulja-itertools/

def permutations(s):
    res = set([s])
    if len(s) == 2:
        res.add(s[1] + s[0]) 
    if len(s) > 2:
        for n, w in enumerate(s):
            for k in permutations(s[:n] + s[n + 1:]):
                res.add(w + k)
    
    return list(res)

strng = 'aabb'
res = []
a = itertools.permutations(strng)
for i in set(a):
    m = ''.join(i)
    print(f'i - {i}\nm - {m}')
    print(type(m))
    res.append(m)
print(res)

def permutations_1(s):
    return list("".join(i) for i in set(itertools.permutations(s)))
# permutations возвращает все варианты перестановки


x = 'aabb' 
#['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
print(permutations(x))
print(permutations_1(x))

