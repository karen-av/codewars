"""
DESCRIPTION:

A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in the Example test fixture.

Your code should be able to compute the first 5 000 
( LC: 400, Clojure: 2 000, Haskell: 12 691, NASM, C, D, C++, Go and Rust: 13 282 ) 
Hamming numbers without timing out.
"""
import datetime

def hamming(n): 
    x = {1}
    print(f'n\n1 - [1, 2, 3, 4]')
    for i in range(1, n):
        m = min(x)
        x.add(m * 2) 
        x.add(m * 3)
        x.add(m * 5)
        x.remove(m)
        print(f'{i + 1} - {sorted(x)}')
    return min(x)

s_time = datetime.datetime.now()
for i in range(20):
    hamming(i)
print(datetime.datetime.now() - s_time)