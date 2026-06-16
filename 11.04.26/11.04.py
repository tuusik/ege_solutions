'''print('a b c d f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((a and b) <= c) and ((b and c) <= d)
                if not f:
                    print(a,b,c,d,f)'''

'''from itertools import product
from math import prod

res = []
for n in product('0123456789', repeat = 4):
    if n[0] != '0' and len(set(n)) == 4:
        n_copy = list(map(int, n))
        n = list(map(int, n))
        first = str(max(n) + min(n))
        n_copy.remove(max(n_copy))
        n_copy.remove(min(n_copy))
        second = str(prod(n_copy))
        r = int(''.join(sorted([first, second])))
        if r > 85:
            res.append(int(''.join(map(str, n))))
print(min(res))'''

'''from turtle import *
lt(90)
tracer(0)
k = 20
screensize(10000, 10000)

for _ in range(7):
    fd(78*k)
    rt(90)
    fd(51*k)
    rt(90)

up()
rt(90)
fd(18*k)
rt(90)
fd(6*k)
down()

for _ in range(3):
    rt(90)
    fd(22*k)
    rt(90)
    fd(44*k)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4, 'red')
done()'''

'''def f(start, end):
    if start == end:
        return 1
    if start > end or start == 25:
        return 0
    if start < end:
        return f(start + 3, end) + f(start * 2, end) + f(start * 5, end)
    
print(f(5, 115))'''

'''def game(s, n):
    if s >= 229 or n > 4:
        return n == 4 or n == 2
    actions = [game(s+2, n+1),
               game(s+3, n+1),
               game(s+4, n+1),
               game(s*2, n+1)]
    if n % 2 == 0:
        return all(actions)
    return any(actions)

for s in range(1, 229):
    if game(s, 0):
        print(s)'''

'''a = [int(num) for num in open('17.txt')]

cnt = 0
max_sum = 0
min3 = sorted([num for num in a if len(str(abs(num))) == 3])
min3 = min(min3[1:])

for i in range(len(a) - 1):
    first, second = a[i], a[i+1]
    if first + second < min3 ** 2:
        cnt += 1
        max_sum = max(max_sum, first + second)

print(cnt, max_sum)'''

'''from itertools import product

cnt = 0

for x in product('ГИПЕРБОЛА', repeat=6):
    x = ''.join(x)
    if x[0] not in 'ИЕОА' and x[5] not in 'ИЕОА':
        x_copy = ''.join(['1' if c in 'ГПРБЛ' else '0' for c in x])
        if '101' not in x_copy:
            cnt += 1
print(cnt)'''

'''l = 42
I = 800 * 1024 
K = 4000
print(I / K)
sn = 204 
print(sn * 8 / l)
i = 38
print(2**i)'''

'''from string import printable

for x in printable[:14]:
    for y in printable[:14]:
        n = int(f'14{y}5{x}2', 14) + int(f'31{x}2{y}3', 14)
        if n % 9 == 0:
            print(int(x, 14) + int(y, 14), n // 9, x)'''

'''from itertools import product

cnt = 0
for x in product('01', repeat = 5):
    x = ''.join(x)
    if x[0] != '1' and '000' not in x and '111' not in x:
        cnt += 1

print(cnt)'''

def f(x, y):
    p1 = x in [2, 3, 6, 13, 26, 39]
    p2 = x in [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    p3 = x in [i for i in range(2, y) if y % i == 0]
    if sum([i for i in range(2, y) if y % i == 0]) == 0:
        return 0
    return (p1 <= p2) or (not p3)

for y in range(2, 1000):
    if all(f(x, y) == 1 for x in range(0, 100000)):
        print(y)