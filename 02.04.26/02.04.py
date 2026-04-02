'''print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))
                if f == 1:
                    print(w, x, y, z, f)

w x y z f
0 0 1 0 True
0 0 1 1 True
0 1 1 1 True'''

'''res = []

for n in range(19, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    res.append(r)
print(min(res))'''

'''from turtle import *

tracer(0)
lt(90)
k = 20
screensize(4000, 4000)

for _ in range(2):
    fd(k)
    lt(270)
    fd(16 * k)
    rt(90)

up()

bk(4*k)
rt(90)
fd(10*k)
lt(90)

down()

for _ in range(2):
    fd(17*k)
    rt(90)
    fd(7*k)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(4, 'red')
done()'''

'''from itertools import product

cnt = 0

for x in product('0123456', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('0') == 1 and x.count('1') <= 2:
        cnt += 1

print(cnt)'''

'''f = open('9_27764.txt')
a = [list(map(int, line.split())) for line in f]
cnt = 0

for line in a:
    if len(set(line)) == len(line):
        if 2 * (max(line) + min(line)) == sum(line) - max(line) - min(line):
            cnt += 1

print(cnt)'''

'''from string import printable

for x in printable[:22]:
    n = int(f'12313{x}57', 22) + int(f'1{x}34561', 22)
    if n % 21 == 0:
        print(x, n / 21)'''