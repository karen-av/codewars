def max_sequence(arr):

    arr_a, arr_b, arr_c, arr_new = [], [], [], []
    arr_a.extend(arr)
    arr_b.extend(arr)
    arr_new.append(sum(arr))

    for i in range(len(arr) - 1):
        arr_a.pop(0)
        arr_new.append(sum(arr_a))

        """
        arr_b.pop()
        arr_new.append(sum(arr_b)) """
        
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


x = max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])
print(f'\n res --  {x}\n')