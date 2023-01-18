def permutations(s):
    i, n = 0, 0
    r = s
    res = [s]
    if len(s) == 0:
        return []
    if len(s) == 1:
        return list(s)
    if len(s) == 2:
        res = [(s[0]+s[1]), (s[1]+s[0])]
        return res
    n = 0
    while n < len(s) - 1:
        r += r[0]
        r = r[1:]
        i += 1
        
        if i == len(s):
            print(n, r)
            w1 = r[n]
            w2 = r[n + 1]
            r = r[2:]
            r = w2 + w1 + r
            n += 1
            i = 0
            print(r,res)
        
        res.append(r)
    result = []
    for i in res:
        if i not in result:
            result.append(i)

    return result

x = 'aabb' 
print(permutations(x))
print(f"['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']")
