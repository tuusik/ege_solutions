'''t = 180
k = 2
b = 8
f = 24_000
print(f * b * k * t / 48_000)
#1440'''

'''N = 70
i = 7
K = 1142
I = 305 * 1024
sn = 274
print(sn * 8 / i)
l = 313'''

'''F = [0 for _ in range(2025)]

for n in range(1, 2025):
    if n == 1: 
        F[n] = 1
    else: 
        F[n] = n * F[n-1]

print((F[2024] - 2 * F[2023]) / F[2022])'''

'''f = open('17_27629.txt')
a = [int(line) for line in f]
cnt = 0
max_pair = 0
max43 = max([num for num in a if abs(num) % 100 == 43 and len(str(abs(num))) == 4])
for i in range(len(a) - 1):
    first, second = a[i], a[i+1]
    if len(str(abs(first))) == 4 or len(str(abs(second))) == 4:
        if (first + second) ** 2 < max43 ** 2:
            cnt += 1
            max_pair = max(max_pair, (first + second) ** 2)
print(cnt, max_pair)'''

'''
def game(f, s, n):
    if f + s >= 207 or n > 4:
        return n == 2 or n == 4
    actions = [game(f + 1, s, n + 1),
               game(f * 2, s, n + 1),
               game(f, s + 1, n + 1),
               game(f, s * 2, n + 1)]
    if n % 2 == 0:
        return all(actions)
    return any(actions)

for S in range(2, 190):
    if game(17, S, 0):
        print(S)'''

'''def f(start, end):
    if start == end:
        return 1
    if start < end:
        return 0
    if start > end:
        return f(start - 1, end) + f(start // 2, end)
    
print(f(40, 16) * f(16, 6))'''

from itertools import product
cnt = 0
for x in product('01', repeat=12):
    x = ''.join(x)
    if (x.count('1') + 7) % 2 == 0:
        cnt += 1
print(cnt)