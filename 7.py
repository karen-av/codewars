"""
Complete the solution so that the function will break up camel casing, using a space between words.
"""

def solution(s):
    string = ''
    for i in s:
        if i.isupper():
            string += ' ' + i
        else:
            string += i
    return string

x = ""
print(f'new word - {solution(x)}')

"""
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""