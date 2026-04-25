'''print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x and (not y)) or (y == z) or w
                if not f:
                    print(w, x, y, z, sum([f, 0]))

w x y z f
0 0 0 1 0
0 0 1 0 0
0 1 1 0 0'''

'''for n in range(1, 10000):
    r = bin(n)[2:]
    if r.count('1') % 2 != 0:
        r += '1'
    else:
        r += '0'
    r = str(int(r, 2))
    r += r[-1]
    r = int(r)
    if r > 1200:
        print(r)
        break'''

'''from turtle import *

k = 20
screensize(10000, 10000)
tracer(0)
lt(90)

for _ in range(2):
    fd(10 * k)
    rt(90)
    fd(18 * k)
    rt(90)

up()
fd(5 * k)
rt(90)
fd(14 * k)
lt(90)
down()

for _ in range(2):
    fd(17 * k)
    rt(90)
    fd(7 * k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(4, 'red')

done()'''

'''x = 1920
y = 1080
i = 16
I = 4 * 1024 * 1024 * 1024 * 8
K = 5_915_000
print(I / x / y / i)
k1 = 1035
print(K / k1)'''

'''from itertools import product

for i, x in enumerate(product(sorted('МЫСЛЬ'), repeat= 5), 1):
    x = ''.join(x)
    if x[:2] == 'ЫЫ':
        print(i, x)'''

'''l = 2500
N = 16510
i = 15
print(l * i / 8)
sn = 4688
K = 65_536
print(K * sn / 1024 / 1024)

print(str('101' * 10 + '01' * 22 + '0').count('1'))'''

'''from string import printable
#14 надо разобрать
def f():
    for p in range(8, 37):
        for T in printable[:p]:
            for H in printable[:p]:
                for N in printable[:p]:
                    for Q in printable[:p]:
                        for U in printable[:p]:
                            for L in printable[:p]:
                                if (int(f'{T}{H}', p) + int(f'{N}{Q}', p) + int(f'{U}', p)) == int(f'1{L}7', p) and len(set([T, H, N, Q, U, L])) == 6 and all(int(x, p) != 7 and int(x, p) != 1 for x in [T, H, N, Q, U, L]):
                                    print(T, H, N, Q, U, L, p, sep = '\n')
                                    return 
f()'''

'''def f(x, A):
    p1 = x % 2 == 0
    p2 = x % 3 == 0
    p3 = x + A >= 100
    return (p1 <= (not p2)) or p3

for A in range(1, 1000):
    if all(f(x, A) is True for x in range(1, 1_000_000)):
        print(A)
        break'''

'''f = [0] * 110
for n in range(110):
    if n <= 3:
        f[n] = n
    elif n > 3 and n <= 32:
        f[n] = n // 4 + f[n - 3]
    else:
        f[n] = 2 * f[n - 5]
print(f[100])'''

'''a = [int(num) for num in open('17_11481.txt')]

cnt = 0
max8 = max([num for num in a if str(abs(num))[0] == '8'])
min_sum = 300_000

for i in range(len(a) - 2):
    check = sum([1 for num in a[i:i+3] if str(abs(num))[0] == '6'])
    if check <= 1 and sum(a[i:i+3]) >= max8:
        cnt += 1
        min_sum = min(min_sum, sum(a[i:i+3]))

print(cnt, min_sum)'''

'''def game(s, n):
    if s >= 37 or n > 4:
        return n == 4 or n == 2
    actions = [game(s + 1, n + 1),
               game(s + 2, n + 1),
               game(s * 3, n + 1)]
    if n % 2 == 0:
        return all(actions)
    return any(actions)

for s in range(37):
    if game(s, 0):
        print(s)'''

'''def f(start, end):
    if start == end:
        return 1
    if start > end or start == 8:
        return 0
    if start < end:
        return f(start + 1, end) + f(start + 2, end)
    
print(f(3, 13))'''

a = [list(map(int, line.split())) for line in open('9-koord_5728.txt')]

cnt = 0

for line in a:
    check1 = all(c > 0 for c in line)
    check2 = all(c < 0 for c in line)
    check3 = all(x < 0 for x in line[::2]) and all(y > 0 for y in line[::-2])
    check4 = all(x > 0 for x in line[::2]) and all(y < 0 for y in line[::-2])
    check5 = all(c > 0 for c in line[:2]) and all(c < 0 for c in line[2:])
    check6 = all(c > 0 for c in line[2:]) and all(c < 0 for c in line[:2])
    check7 = (line[0] < 0 and line[1] > 0) and (line[2] > 0 and line[3] < 0)
    check8 = (line[0] > 0 and line[1] < 0) and (line[2] < 0 and line[3] > 0)
    if check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8:
        cnt += 1
print(cnt)