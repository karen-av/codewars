
def func(text, chr):
    return(chr.join(text))

def func1(text, chr):
    res = ''
    for word in text.split():
        res += "_".join(word)
        res += ' '
    res = res[:-1]
    return res

def func2(text, chr):
    x = ("_".join(word) for word in text.split())
    res = ''
    for i in x:
        res += (i + ' ')
    return res


x = 'next'
y = 'hello world'
print(func(x, '_'))
print(func1(y, "_"))
print((func2(y, '_')))

a = (i**2 for i in range(1,5))
for i in a:
 pass
#   print(i)