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

def permutations(s):
    res = []
    for w in s:
        tmp_res = s[0] + s[1]
        res.append(tmp_res)
        
    return res

x = 'ab'
print(permutations(x))
