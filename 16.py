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
    strng = s
    res = []
    c = 0
    while c < len(s):
        i = 0
        while i < len(s):
            tmp_res = ''
            for word in strng:
                tmp_res += word
            strng += strng[0]
            strng = strng[1:]

            res.append(tmp_res)
            i += 1
        
        strng += strng[0]
        strng = strng[1:]
        c += 1

    return res

x = 'aabb' 
#['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
print(permutations(x))
