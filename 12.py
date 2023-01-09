"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. 
It should follow the API demonstrated in the examples below. Multiple roman numeral values 
will be tested for each helper method.
Modern Roman numerals are written by expressing each digit separately starting with the left 
most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 
1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; 
or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
Symbol	Value
I	1
IV	4
V	5
X	10
L	50
C	100
D	500
M	1000
"""

class RomanNumerals:
    
    def to_roman(val):
        val = str(val)
        res = ''

        length = len(val)
        if length == 4:
            for i in range(int(val[0])):
                res += 'M'
            val = val[1:]

        if int(val[0]) != 0 and length >= 3:
            if int(val[0]) >= 1 and int(val[0]) <= 3:
                for d in range(int(val[1])):
                    res += 'C'
            elif int(val[0]) != 0 and int(val[0]) == 4:
                res += 'CD'
            elif int(val[0]) != 0 and int(val[0]) == 5:
                res += 'D'
            elif int(val[0]) >= 6 and int(val[0]) <= 8:
                res += 'D'
                for d in range(int(val[1]) - 5):
                    res += 'C'
            elif int(val[0]) >= 9:
                res += 'CM'
            val = val[1:]
        elif int(val[0]) == 0 and length >= 3:
            val = val[1:]

        if int(val[0]) != 0 and length >= 2:
            if int(val[0]) == 1:
                res += 'X'
            elif int(val[0]) >= 2 and int(val[0]) <= 3:
                for i in range(int(val[0])):
                    res += 'X'
            elif int(val[0]) == 4:
                res += 'XL'
            elif int(val[0]) == 5:
                res += 'L'
            elif int(val[0]) >= 5 and int(val[0]) <= 8:
                res += 'L'
                for i in range(int(val[0]) - 5):
                    res += 'X'
            elif int(val[0]) >= 9:
                res += 'XC'
            val = val[1:]
        elif int(val[0]) == 0 and length >= 2:
            val = val[1:]

        if int(val[0]) != 0 and length >= 1:
            if int(val[0]) >= 1 and int(val[0]) <= 3:
                for i in range(int(val[0])):
                    res += 'I'
            elif int(val[0]) == 4:
                res += "IV"
            elif int(val[0]) == 5:
                res += 'V'
            elif int(val[0]) >= 5 and int(val[0]) <= 8:
                res += "V"
                for i in range(int(val[0]) - 5):
                    res += 'I'
            elif int(val[0]) >= 9:
                res += 'IX'

        return res
            

    def from_roman(roman_num):
        return 0


x = 3999
print(RomanNumerals.to_roman(x))
print(RomanNumerals.from_roman(x))