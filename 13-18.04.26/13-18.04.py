'''print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x and y) <= (not z)) and (x <= y) or w
                if not f:
                    print(x, y, z, w, int(f))
    
x y z w f
1 0 0 0 0
1 0 1 0 0
1 1 1 0 0'''

'''def quadro(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s

res = []

for n in range(1, 10000):
    r = quadro(n)
    if n % 4 == 0:
        r += r[-2:]
    else:
        r += quadro((r.count('1') + r.count('2') * 2 + r.count('3') * 3) * 4)
    r = int(r, 4)
    if r % 2 == 0 and r > 211 and r % 3 == 0:
        res += [r]

print(res)'''

'''x = 1920
y = 1080
i = 16
s = 1474560
k = 300
print(x * y * i * k / s / 60)'''

'''from itertools import permutations
cnt = 0
for x in permutations('ПРОФИМАТИКА', 11):
    x = ''.join(x)
    if x[0] != 'П' and 'ИИ' not in x:
        cnt += 1
print(cnt / 4)'''

'''a = [list(map(int, line.split())) for line in open('9.txt')]
for i, line in enumerate(a, 1):
    rep = [num for num in line if line.count(num) == 3]
    uniq = [num for num in line if line.count(num) == 1]
    if len(rep) == 3 and max(line) in rep and max(line) % 10 == 0 and len(uniq) == 4:
        print(i)
        break'''

'''l = 4403
K = 5845627
I = 15 * 1024 * 1024 * 1024
print(I / K)
sn = 2756
print(sn * 8 / l)
i = 6'''

'''print(bin(67)[2:])

print(int('10111100', 2))'''

'''from string import printable

def ss28(n):
    s = ''
    while n > 0:
        s = printable[n % 28] + s
        n //= 28
    return s

d = {}

for x in range(1, 28_001):
    n = 4 * 28**10 + 3 * 28**6  + 28**3 - x
    r = ss28(n)
    d[n] = r.count('0')

print(sorted(d.items(), key= lambda x: x[1]))'''

'''g = [-1] * 260_001
for n in range(260_000, 0, -1):
    if n >= 250_000:
        g[n] = n // 20 + 45
    elif n < 250_000:
        g[n] = g[n + 9] - 2

f = [-1] * 700
for n in range(700):
    if n >= 25:
        f[n] = f[n - 6] + 4137
    elif n < 25:
        f[n] = 7 * (g[n - 9] - 40)

print(f[680])'''

'''def game(f, s, n):
    if f + s >= 81 or n > 4:
        return n == 4 or n == 2
    actions = [game(f + 1, s, n + 1),
               game(f * 2, s, n + 1),
               game(f, s + 1, n + 1),
               game(f, s * 2, n + 1)]
    if n % 2 == 0:
        return all(actions)
    return any(actions)

for s in range(1, 74):
    if game(7, s, 0):
        print(s)'''

'''a = list(map(int, open('17.txt')))

cnt = 0
max42 = max([num for num in a if abs(num) % 100 == 42])
max_sum = 0

for i in range(len(a) - 2):
    check = len([num for num in a[i:i+3] if len(str(abs(num))) == 3 and abs(num) % 10 == 9])
    if check == 1:
        if sum(a[i:i+3]) > max42:
            cnt += 1
            max_sum = max(max_sum, sum(a[i:i+3]))

print(cnt, max_sum)'''

def f(start, end, prev):
    if start == end:
        return 1
    if start > end:
        return 0
    if start < end:
        if prev == 1:
            return f(start + 2, end, 2) + f(start + 4, end, 4) + f(start + 8, end, 8)
        if prev == 2:
            return f(start + 1, end, 1) + f(start + 4, end, 4) + f(start + 8, end, 8)
        if prev == 4:
            return f(start + 2, end, 2) + f(start + 1, end, 1) + f(start + 8, end, 8)
        if prev == 8:
            return f(start + 2, end, 2) + f(start + 4, end, 4) + f(start + 1, end, 1)
        if prev == 0:
            return f(start + 1, end, 1) + f(start + 2, end, 2) + f(start + 4, end, 4) + f(start + 8, end, 8)
        
print(f(16, 48, 0))