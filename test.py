
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
    return(chr.join(word) for word in text.splir())

x = 'next'
y = 'hello world'
print(func(x, '_'))
print(func1(y, "_"))
print(y, '_')