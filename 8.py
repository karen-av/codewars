"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
"""

def create_phone_number(n):
    #your code here
    number = ''
    for i, num in enumerate(n):
        num = str(num)
        if i == 0:
            number += '(' + num
        elif i == 3:
            number += ')' + ' ' + num
        elif i == 6:
            number += '-' + num
        else:
            number += num
            
    return number

def not_my(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(x))