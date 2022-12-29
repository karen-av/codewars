def find_short_0(s):
    list_l = []
    dig = 0
    for l, word in enumerate(s):
        if word != ' ':
            dig +=1
            if len(s) == l+1:
                list_l.append(dig)
        else:
            list_l.append(dig)
            dig = 0
    return min(list_l)

def find_short(s):
    return min(len(x) for x in s.split())

x = find_short("Let's travel abroad shall we")
print(x)