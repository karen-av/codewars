def dig_pow(n, p):
    num = 0
    for index, dig in enumerate(str(n)):
        num += int(dig)**(p+index)
    return num/n if num%n == 0 else -1

a = 1
b = 1
x = dig_pow(a, b)
print(f'x = {x}')