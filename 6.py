
def test(arr):
    if len(arr) == 0:
        return 0

    pos, neg, i = 0, 0, 0
    while (pos == 0 and neg == 0) or i < len(arr):
        if arr[i] > 0:
            pos = 1
        elif arr[i] <= 0:
            neg = 1
        i += 1
    if pos > 0 and neg == 0:
        return sum(arr)
    elif neg > 0 and pos == 0:
        return 0
    else:
        
        arr_new = []
        for i, n in enumerate(arr):
            summa = 0
            for ii in range(len(arr) - i):
                num = ii + i
                summa += arr[num]
                if i != 0 and i != len(arr):
                    arr_new.append(summa)
        return max(arr_new)

def max_sequence(arr):
    maximum = 0
    local_maximum = 0
    for i in arr:
        if local_maximum > 0:
            local_maximum += i
            if local_maximum < 0:
                local_maximum = 0
            elif local_maximum > maximum:
                maximum = local_maximum
        elif i > 0:
            local_maximum += i

    return maximum

def test_new(arr):
    max, max_tmp = 0, 0
    for i in arr:
        if max_tmp > 0:
            pass
        elif max_tmp < 0:
            pass

    return max

c = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43] #155
x =[-2, -1, -3, -4, -1, -2, -1, -5, -4] #0
zero = []
positive = [1, 3, 5, 30, 50] #89
m =     [-2, 1, -3, 4, -1, 2, 1, -5, 4] #6
m_new = [-2, 1, -3, 4, -1, 2, 1, -7, 10] #6


#cc = test(c)
#xx = test(x)
#zer = test(zero)
#pos = test(positive)
#mm = test(m)
#print(f'cc - {cc}')
#print(f'x - {xx}')
#print(f'zer = {zer}')
#print(f'pos - {pos}')
#print(f'm - {mm}')

my = test(m_new)
nn = max_sequence(m_new)
print(f'my - {my}\nnn - {nn}')
