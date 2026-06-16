'''def f(x, A):
    p1 = x % 128 == 0
    p2 = x % A == 0
    p3 = x % 80 == 0
    return p1 <= ((not p2) <= (not p3))

for A in range(1, 1000):
    if all(f(x, A) == 1 for x in range(1, 10000)):
        print(A)'''

'''f = [0] * 50
for n in range(1, 50):
    if n < 3:
        f[n] = 2
    elif n > 2 and n % 2 == 0:
        f[n] = f[n - 2] - f[n - 1] + 2
    elif n > 2 and n % 2 != 0:
        f[n] = f[n - 1] - f[n - 2] - 2

print(f[29]) '''

'''def game(s, n):
    if s >= 100 or n > 2:
        return n == 2
    actions = [game(s * 2, n + 1),
               game(s * 3, n + 1)]
    if n % 2 == 0:
        return all(actions)
    return any(actions)

for s in range(1, 100):
    if game(s, 0):
        print(s)'''

'''def f(start, end):
    if start == end:
        return 1
    if start < end:
        return 0
    if start > end:
        return f(start - 4, end) + f(start // 3, end)

print(f(36, 2))'''

'''n = 5 * 216**1156 - 4 * 36**1147 + 6**1153 - 875
r = ''
while n > 0:
    r = str(n % 6) + r
    n //= 6
print(r.count('5') - r.count('0'))'''

'''cnt = 0
for x in range(1_000_000, 10_000_000):
    r = ''
    while x > 0:
        r = str(x % 9) + r
        x //= 9
    p = ''.join(['0' if int(n) % 2 == 0 else '1' for n in r])
    if r.count('6') == 1 and '11' not in p and '00' not in p:
        cnt += 1
print(cnt)'''

'''print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not (y and (not x))) and (not (x == z)) and w
                if f:
                    print(w, x, y, z, f)
                    
w x y z f
1 0 0 1 1
1 1 0 0 1
1 1 1 0 1'''

res = []

def triple(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(1, 10000):
    r = triple(n)
    if n % 3 == 0:
        r += r[:3]
    else:
        r += triple((r.count('1') + r.count('2') * 2) * 5)
    r = int(r, 3)
    if r % 2 == 1 and r > 2500:
        res += [r]

print(min(res))