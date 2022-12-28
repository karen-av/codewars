def count_bits(n):
    list = []
    sum = 0
    while n >= 1:
        x = n % 2
        if x == 0:
            list.append(0)
        else:   
            list.append(1)
        n = int(n / 2)
    list.reverse()
    print(list)
    for i in list:
        if i == 1:
            sum += 1
    return sum

a = 0
while a == 0:
    x = -1
    while int(x) < 0:
        y = input('Number:_')
        if y.isdigit():
            x = y
        
    binary = count_bits(int(x))
    print(f"Binary - {binary}\nDone V\n")

