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

def permutations(s):
    res = set([s])
    print(f'res - {res}')
    if len(s) == 2:
        res.add(s[1] + s[0]) 
    if len(s) > 2:
        for n, w in enumerate(s):
            for k in permutations(s[:n] + s[n + 1:]):
                res.add(w + k)
    
    return list(res)

def permutations_1(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

x = 'aabb' 
#['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
print(permutations(x))
print(permutations_1(x))

