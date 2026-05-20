'''
print("w x y z F")

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((x <= y) and (z or w)) <= ((x == w) or (y and (not z))):
                    F = 1
                else:
                    F = 0
                print(w, x, y, z, F)

w x y z F
0 1 1 1 0
1 0 0 0 0
1 0 0 1 0
1 0 1 1 0
'''

'''
for N in range(1, 1000):
    n = N
    r = ''
    while n > 0:
        r = str(n%5) + r
        n //= 5
    if len(r) % 2 == 0:
        mid = len(r) // 2
        g = r[mid:] + r[:mid]
    else:
        r = r + str(N%5)
        mid = len(r) // 2
        g = r[mid:] + r[:mid]
    if int(g, 5) > 50:
        print(N)
'''

'''
from turtle import *

k = 10
tracer(0)

for i in range(15):
    fd(3*k)
    right(40)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3, 'red')
done()
'''
'''
from itertools import *
k = 0 
suma = 0 
for x in sorted(product('СДАЙЕГЭ', repeat=6)):
    s = ''.join(x) 
    k += 1 
    if 'ЕГЭ' in s: 
        suma += k 
print(suma)
'''
'''
def f(x):  
    P = 5 <= x <= 280  
    Q = 295 <= x <= 400  
    R = 375 <= x <= 450  
    A = a1 <= x <= a2  
    return (Q <= P) or ((not A) <= R)  

r = []  
d = [y for x in (5, 280, 295, 400, 375, 450) for y in (x - 0.1, x, x + 0.1)]  
for a1 in d:  
    for a2 in d:  
        if a1 <= a2 and all(f(x) for x in d):  
            r += [a2 - a1]  
print(min(r))  
'''

from functools import lru_cache

@lru_cache(None)
def F(n):
    
    if n > 1000000:
        return n
    return n + F(2 * n)

def G(n):
    return F(n) / n

g2000 = G(2000)

count = 0                   
for n in range(1000, 1000001):    
    if G(n) == g2000:       
        count += 1

print(count)     




























