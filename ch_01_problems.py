# -*- coding: utf-8 -*-
from plotting import plot

S = {2 + 2j,
     3 + 2j,
     1.75 + 1j,
     2 + 1j,
     2.25 + 1j,
     2.5 + 1j,
     2.75 + 1j,
     3 + 1j,
     3.25 + 1j}

plot(S, 4)

# 1.4.7
plot({s*2 for s in S}, 8)

# 1.4.8
plot({s*0.5j for s in S}, 4)

# 1.4.9
plot({2-1j+s*0.5j for s in S}, 4)

# 1.4.10
from image import file2image

i = file2image('img01.png')

y = len(i)
x = len(i[0])

d = {xi + (y-yi) * 1j for yi in range(y) for xi in range(x) if i[yi][xi][0]<120}
plot(d, max(y, x))

# 1.4.11 /12
def center(S):
    max_x = max([_.real for _ in S])
    max_y = max([_.imag for _ in S])
    trans = max_x * -0.5 + max_y * -0.5 * 1j
    d = [_ + trans for _ in S]
    plot(d, max(max_x/2, max_y/2))
    
center(S)
    
# 1.4.17
from math import e, pi
n = 20
W = {e**((2*pi*1j)/n) for n in range(1, n)}
plot(W)

# 1.4.18
t = pi/4
S1 = {_*e**(t*1j) for _ in S}
plot(S1)

# 1.4.19
d1 = {_*e**(t*1j) for _ in d}
plot(d1, max(y, x))

# 1.4.20
max_x = max([_.real for _ in d])
max_y = max([_.imag for _ in d])
trans = max_x * -0.5 + max_y * -0.5 * 1j
d2 = {0.5*(_+trans)*e**(t*1j) for _ in d}
plot(d2, 150)

# 1.5 - didn't finish :(
idx = {n: a for a, n in zip(list('abcdefghijklmnopqrtsuvwxyz '), range(27))}
def get_bin(num):
    return format(num, '05b')

M = ['10101',
     '00100',
     '10101',
     '01011',
     '11001',
     '00011',
     '01011',
     '10101',
     '00100',
     '11001',
     '11010']
    
def get_letter(letter_bitstring):
    index_num = get_index(int(letter_bitstring, 2))
    return idx[index_num]
    
def get_index(num):
    if num <= 26:
        return num
    else:
        return num%26-1

from GF2 import one

key = one
def decrypt(letter_bitstring):
    x = [int(_) for _ in letter_bitstring]
    y = []
    for _ in x:
        if _ == 1:
            y.append(one + key)
        else:
            y.append(0 + key)
    y = ['1' if _==one else '0' for _ in y]
    return ''.join(y)
    
for m in M:
    print(decrypt(m))
    
# 1.7.1
def my_filter(L, num):
    return [_ for _ in L if _%num!=0]

my_filter([1, 2, 4, 5, 7], 2)

# 1.7.2
def my_lists(L):
    return [[b for b in range(1, a+1)] for a in L]

my_lists([1, 2, 4])

# 1.7.3
def my_function_composition(f, g):
    return {_: g[f[_]] for _ in f.keys()}

f = {0: 'a', 1: 'b'}
g = {'a': 'apple', 'b': 'banana'}

my_function_composition(f, g)

# 1.7.4
def mySum(L):
    current = None
    for x in L:
        if not current:
            current = x
        current += x
    return current

mySum([1, 2, 3])

# 1.7.5
def myProduct(L):
    current = None
    for x in L:
        if not current:
            current = x
        current *= x
    return current
     
myProduct([2, 4, 6])

# 1.7.6
def myMin(L):
    current = None
    for x in L:
        if not current:
            current = x
        elif x < current:
            current = x
    return current

myMin([-10, 10, 100])

# 1.7.7
def myConcat(L):
    current = None
    for x in L:
        if not current:
            current = x
        current += x
    return current

myConcat(['m', 'a', 't', 'r', 'i', 'x'])

# 1.7.8
def myUnion(L):
    current = []
    for x in L:
        for y in x:
            if y not in current:
                current.append(y)
    return current

myUnion([{0, 1, 2}, {1, 2, 3}])


 

        