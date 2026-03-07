'''
print('w x y z f1 f2')


def f1(w, x, y, z, F1):
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if (w == x) and (y<=z):
                        F1 = 1
                    else:
                        F1 = 0
                    return w, x, y, z, F1

def f2(w, x, y, z, F2):
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if (w <= x) <= (y == z) :
                        F2 = 1
                    else:
                        F2 = 0
                    return w, x, y, z, F2
'''
'''
for n in range(256):
    b = n
    N = bin(n)[2:]
    if len(N) == 8:
        a = str(N)[:2] + str(N)[6:]
        R = int(a, 2)
        if R == 7:
            print(R)
'''

'''
from turtle import *

k = 20

for i in range(36):
    forward(10*k)
    right(50)

done()
'''

'''
def f(x):
    p = 117 <= x <= 158
    q = 129 <= x <= 180
    A = a1 <= x <= a2
    return p <= ((q and (not (A))) <= (not (p)))

rez = []

for a1 in range(1000):
    for a2 in range(a1, 1000):
        A = range(a1, a2 + 1)
        if all(f(x) == 1 for x in range(1000)):
            rez.append(a2-a1)
print(min(rez))
'''
'''
def f(n):
    if n < 50:
        return n
    if n > 49:
        return 2 * g(50-n//2)
def g(n):
    if n > 40:
        return 10
    if n < 41:
        return 30 + f(n + 600 // n)

print(f(80))
'''

#субботний
'''
rez = []
for N in range(10000):
    n = bin(N)[2:]
    for i in range(2):
        if (str(N).count('1')+ str(N).count('2')*2+ str(N).count('3')*3+ str(N).count('4')*4+ str(N).count('5')*5+ str(N).count('6')*6+ str(N).count('7')*7+ str(N).count('8')*8+ str(N).count('9')*9) %2 == 0:
            a = n + '0'
        else:
            a = n + '1'
        R = int(a, 2)
        
        if R > 2054:
            rez.append(R)

print(min(rez))
'''

'''
from turtle import *

tracer(0)
k = 20
for i in range(15):
    forward(4*k)
    right(60)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4, 'red')
done()
'''
'''
from itertools import *

k = 0

for i in set(permutations('КИДАЛА', 5)):
    m = True
    a = ''.join(i)
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            m = False
    if m == True:
        k += 1
print(k)
'''
'''
for p in range(10, 30):
    for x in range(p):
        for y in range(p):
            if (5*p**3 + x*p**2 + 8*p + 3) + (x*p**3 + 9*p**2 + x*p + 9) == (y*p**3 + 2*p**2 + y):
                print(x*p**2 + y*p + y)
                '''

from sys import setrecursionlimit

setrecursionlimit(100000)

def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n%2 == 0:
        return f(n + 2)-3
    if n < 10000 and n%2 != 0:
        return f(n + 2)+1
print(f(94)- f(80)) 