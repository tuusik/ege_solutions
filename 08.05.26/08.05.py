'''print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = w or (y and (not x)) or (not z)
                if not f:
                    print(w, x, y, z, int(f))'''

'''res = []

for n in range(42, 1000):
    r = bin(n)[2:]
    if n % 2 == 1:
        r = '10' + r
        r = r[:-2] + '01'
    else:
        r += '1'
        r = '11' + r[2:]
    r = int(r, 2)
    res += [r]

print(min(res))'''

'''from turtle import *

tracer(0)
screensize(10000, 10000)
k = 20

lt(90)

for _ in range(2):
    fd(12*k)
    rt(90)
    fd(7*k)
    rt(90)

up()
fd(5*k)
rt(90)
down()

for _ in range(2):
    fd(4*k)
    rt(90)
    fd(9*k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4, 'red')
done()'''

'''from itertools import product

for i, x in enumerate(product(sorted('ЛЕГКО'), repeat= 6), 1):
    x = ''.join(x)
    if x.count('Г') >= 2 and 'ГГ' not in x:
        print(i, x)'''

'''a = [list(map(int, line.split())) for line in open('9.txt')]

for i, line in enumerate(a, 1):
    rep = [num for num in line if line.count(num) == 3]
    not_rep = [num for num in line if line.count(num) == 1]
    if len(rep) == 3 and len(not_rep) == 4:
        line_copy = sorted(line, reverse= True)
        if line_copy[0] + line_copy[1] > sum(line_copy[2:]):
            print(i, line)'''

'''a = 4098
i = 13
I = 12 * 1024
k = 186
print(I / k)
b = 66
print(b * 8 / i)'''

'''from string import printable

def f(n):
    r = ''
    while n > 0:
        r = printable[n % 36] + r
        n //= 36
    return r

n = 5 * 1296**597 + 8 * 216**314 - 4 * 36**215 + 9 * 6**214 - 7 * 6**18 - 54
n = f(n)
cnt = 0
for i in range(8):
    cnt += n.count(str(i))
print(cnt)'''

'''def f(x, y, A):
    p1 = 2*x - y >= A
    p2 = y >= 17
    p3 = x <= 78
    return p1 and p2 and p3

for A in range(1000):
    if all(f(x, y, A) == 0 for x in range(1000) for y in range(1000)):
        print(A)'''

'''f = [0] * 7100

for n in range(7010, 0, -1):
    if n >= 7000:
        f[n] = n
    elif n < 7000:
        f[n] = f[n + 2] + n + 3

print(f[52] - f[56])'''