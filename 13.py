"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal 
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range 
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

def rgb(r, g, b):
    res = ''
    
    dict = {
    0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'
    }
    for i in  r, g, b:
        res_loc = ''
        if i > 255: 
            i = 255
        if i < 0: 
            i = 0
        if i == 0: 
            res_loc = '00'
        while i >= 1:
            res_loc = dict[int(i % 16)] + res_loc
            i = i / 16
        if len(res_loc) == 1:
            res_loc = '0' + res_loc
        res += res_loc
    return res


r = 0
g = 3
b = 4
x = rgb(r, g, b)
print(x)