s = '0123456789'
x = s[3:] # delete first 3
y = s[-3:] # save last 3
z = s[:3] # save first 3
a = s[:-3] # delete last 3
f = s[2:7:2]
print(f'x - {x}\ny - {y}\nz - {z}\na - {a}\nf - {f}')


a = [1, 3, 8, 7]
print(a[::-1])
#[7, 8, 3, 1]
print(a[:-2])
#[1, 3]
print(a[-2::-1])
#[8, 3, 1]
print(a[:1:])
#[]

a = ['abcd']
print(a)
s = set(a)
print(s)
l = list(s)
print(l)