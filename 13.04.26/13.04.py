'''print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not (((not x) or y) and (not w))) or (not (z and (not (y and w))))
                if not f:
                    print(w,x,y,z,f)
w x y z f
0 0 0 1 False
0 0 1 1 False
0 1 1 1 False'''

'''def triple(n):
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

res = []

for n in range(1, 1000):
    r = triple(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += triple(r.count("1") + r.count("2") * 2)
    r = int(r, 3)
    if r > 220:
        res.append(r)

print(min(res))'''

'''from turtle import *
tracer(0)
k = 20
screensize(10000, 10000)
lt(90)

for _ in range(8):
    fd(16*k)
    rt(90)
    fd(22*k)
    rt(90)

up()
fd(5*k)
rt(90)
fd(5*k)
lt(90)
down()

for _ in range(8):
    fd(52*k)
    rt(90)
    fd(77*k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4, 'red')

done()'''

'''f = [0] * 14_000
for n in range(14_000):
    if n < 5:
        f[n] = n
    else:
        f[n] = 2 * n * f[n - 4]
print((f[13766] - 9 * f[13762]) / f[13758])'''

'''def f(x, y, A):
    p1 = x - 3 * y < A
    p2 = y > 400
    p3 = x > 56
    return p1 or p2 or p3

for A in range(1000):
    if all(f(x, y, A) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        print(A)'''

'''from string import printable

for x in printable[:25]:
    n = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if n % 24 == 0:
        print(x, n // 24)'''

'''l = 377
K = 23155
I = 5536 * 1024
print(I / K)
sn = 245
print(sn * 8 / l)
i = 6'''

'''from itertools import product

for i, x in enumerate(product(sorted('ЯНВАРЬ'), repeat=5), 1):
    x = ''.join(x)
    if x[0] != 'Я' and x.count('Ь') <= 1 and 'ЯЯ' not in x:
        print(i, x)'''

'''a = [list(map(int, line.split())) for line in open('9_19241.txt')]

for i, line in enumerate(a, 1):
    repeat = [num for num in line if line.count(num) == 3]
    if len(repeat) == 6:
        if sum(repeat) / 6 < sum(line) - sum(repeat):
            print(i, line)'''

x = 3840 * 2160
i = 24
#print(x * i / 8 / 1024 )
shot = 24300
print(16 * 1024 * 1024 / shot)
shots_per_flash = 690
K = 3742
while K >= 690:
    K -= 690
print(K)