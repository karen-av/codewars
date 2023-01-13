"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def strip_comments(strng, markers):
    i = 0
    res = ''
    for char in strng: 
        if char in markers:
            i += 1
            if len(res) > 0 and res[-1] != '\n':
                res = res.rstrip()
        if char == '\n':
            i = 0
        if i == 0:
            res += char

    return res

result = strip_comments("\t@\nlemons\nlemons ' avocados bananas\n# ' ' bananas", 
                        ['=', '^', "'", '!', '#', '.', ',', '@', '?']
                        )
print(repr(result))