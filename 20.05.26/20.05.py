'''print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = ((x <= y) and (z or w)) <= ((x == w) or (y and (not z)))
                if not f:
                    print(w, x, y, z, int(f))

w x y z f
0 1 1 1 0
1 0 0 1 0

1 0 0 0 0
1 0 1 1 0
1 0 0 1 0'''

'''def fifth(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s

d = {}

for n in range(1, 1000):
    r = fifth(n)
    l = len(r)
    if l % 2 == 0:
        r = r[l//2:] + r[:l//2]
    else:
        r += str(n % 5)
        l += 1
        r = r[l//2:] + r[:l//2]
    r = int(r, 5)
    if r > 50:
        d[n] = r
print(min(d.keys()))'''
'''
from turtle import *

screensize(10000, 10000)
tracer(0)
lt(90)
k = 20

for _ in range(15):
    fd(3 * k)
    rt(40)

up()

for x in range(1, 50):
    for y in range(1, 50):
        goto(x * k, y * k)
        dot(4, 'red')

done()'''
'''
from itertools import product

cnt = 0

for i, x in enumerate(product(sorted('СДАЙЕГЭ'), repeat= 6), 1):
    x = ''.join(x)
    if 'ЕГЭ' in x:
        cnt += i

print(cnt)'''
'''def f(start, end, num):
    if start == end:
        return 1
    if start < end or start == num:
        return 0
    if start > end:
        return (f(start - 1, end, num) + f(start - 3, end, num) + f(start // 3, end, num))

ans1 = f(49, 40, 20) * f(40, 30, 20) * f(30, 12, 20)
ans2 = f(49, 40, 30) * f(40, 20, 30) * f(20, 12, 30)
ans3 = f(49, 30, 40) * f(30, 20, 40) * f(20, 12, 40)
ans4 = f(49, 40, -1) * f(40, 30, -1) * f(30, 20, -1) * f(20, 12, -1)
print(ans1 + ans2 + ans3 + ans4)'''

'''def game(f, s, n):
    if s >= 40 or f >= 40 or n > 3:
        return n == 3
    if f > s:
        actions = [game(f + 1, s, n + 1),
                   game(f + 2, s, n + 1),
                   game(f + 3, s, n + 1),
                   game(f, s * 2, n + 1)]
    elif f < s:
        actions = [game(f, s + 1, n + 1),
                   game(f, s + 2, n + 1),
                   game(f, s + 3, n + 1),
                   game(f * 2, s, n + 1)]
    else:
        actions = [game(f + 1, s, n + 1),
                   game(f + 2, s, n + 1),
                   game(f + 3, s, n + 1),
                   game(f, s + 1, n + 1),
                   game(f, s + 2, n + 1),
                   game(f, s + 3, n + 1)]
    if n % 2 == 0:
        return any(actions)
    return all(actions)

for s in range(1, 40):
    if game(11, s, 0):
        print(s)'''

'''a = [list(map(int, line.split())) for line in open('9_20070.txt')]

cnt = 0

for line in a:
    check1 = [1 for num in line if len(str(num)) == 2]
    check2 = [1 for num in line if num % 5 != 0]
    if (sum(check1) == 6) != (sum(check2) == 6):
        cnt += 1
print(cnt)'''

'''l = 24
i = int()
I = 170 * 1024
k = 5100
print(I / k )
print(34 / 3)'''

'''from string import printable

def f(n):
    s = 0
    for i in range(0, len(n)):
        s += printable[:37].index(n[~i]) * (37 ** i)
    return s

for x in printable[:37]:
    n = f(f'98{x}31') + f(f'1{x}924')
    if n % 21 == 0:
        print(x, n // 21)'''

'''from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(1_000_010)
cnt = 0
lru_cache(None)
def f(n):
    if n > 1_000_000:
        return n
    if n <= 1_000_000:
        return n + f(2*n)
    
lru_cache(None)
def g(n):
    return f(n) / n

for i in range(1, 1_000_000):
    f(i)
    g(i)
    if g(i) == g(2000):
        cnt += 1
print(cnt)'''

'''a = list(map(int, open('17_14260.txt')))

cnt = 0
max_sum = 0

min_num = min([num for num in a if num > 0 and len(str(abs(num))) == 4 and str(num)[-1] == str(num)[-2]])

for i in range(len(a) - 2):
    check = [1 for num in a[i:i+3] if len(str(abs(num))) == 3]
    print(check, sum(a[i:i+3]))
    if sum(check) == 3 and sum(a[i:i+3]) > min_num:
        cnt += 1
        max_sum = max(max_sum, sum(a[i:i+3]))
print(cnt, max_sum)'''