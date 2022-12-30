import array as arr

def max_sequence(arr):

    arr_a, arr_b, arr_c, arr_new = [], [], [], []
    arr_a.extend(arr)
    arr_b.extend(arr)
    arr_new.append(sum(arr))

    for i in range(len(arr) - 1):
        arr_a.pop(0)
        arr_new.append(sum(arr_a))

        arr_b.pop()
        arr_new.append(sum(arr_b))
        
        arr_a1 = []
        arr_a1.extend(arr_a)
        for ii in range(len(arr_a) - 1):
            arr_a1.pop()
            arr_new.append(sum(arr_a1))
        
        """
        arr_b1 = []
        arr_b1.extend(arr_b)
        for ii in range(len(arr_b) - 1):
            arr_b1.pop(0)
            arr_new.append(sum(arr_b1))
        """ 
    

    return max(arr_new) if max(arr_new) >= 0 else 0

def test(arr):
    if len(arr) == 0:
        return 0
    arr_new = []
    while len(arr) != 0:
        sum = 0
        for i, dig in enumerate(arr):
            sum += arr[i]
            arr_new.append(sum)
            #print(f'i - {i}\nsum - {sum}\n---')
        #arr_new.append("/")
        arr.pop(0)
        #print(f'n - {n}\narr - {arr_new}\n---')
    return max(arr_new) if max(arr_new) >= 0 else 0


x =[-2, -1, -3, -4, -1, -2, -1, -5, -4] #0
y = arr.array('i', [-2, -1, -3, -4, -1, -2, -1, -5, -4])

m = [-2, 1, -3, 4, -1, 2, 1, -5, 4] #6

c = arr.array('i', [-2, 1, -3, 4, -1, 2, 1, -5, 4])
g = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43] #155
zero = []

z =  test(c)
cc = test(g)
xx = test(x)
zer = test(zero)
print(f'res --  {z}\ncc - {cc}\nx - {xx}\nzer = {zer}')