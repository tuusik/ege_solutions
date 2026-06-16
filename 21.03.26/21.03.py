'''f = open('17_2710.txt')
s = [int(num) for num in f]
cnt = 0
max_mod = 0
for i in range(len(s)):
    if i == 0:
        if s[i] < s[i+1]:
            cnt += 1
            max_mod = max(max_mod, abs(s[i] - s[i+1]))
    elif i == len(s) - 1:
        if s[i] < s[i-1]:
            cnt += 1
            max_mod = max(max_mod, abs(s[i] - s[i-1]))
    else:
        if s[i-1] > s[i] < s[i+1]:
            cnt += 1
            max_mod = max(max_mod, max(abs(s[i] - s[i+1]), abs(s[i] - s[i-1])))

print(cnt, max_mod)'''

'''s = [list(map(int, line.split())) for line in open('9_18258.txt')]

max_line = 0

def cnt_dig(n):
    cnt = 0
    while n > 0:
        cnt += n % 10
        n //= 10
    return cnt

cnt = 0

for line in s:
    if line == sorted(line):
        rep = [1 if line.count(num) > 1 and cnt_dig(num) % 2 == 0 else 0 for num in line]
        if sum(rep) != 0:
            max_line = max(max_line, cnt)
    cnt += 1

print(max_line)'''

'''def to_dec(n, ns):
    res = 0
    power = 0
    for i in range(1, len(n) + 1):
        res += n[-i] * (ns ** power)
        power += 1
    return res

res = []
for x in range(10, 67):
    for y in range(0, x):
        n1 = [7, 3, x, 1, y]
        n2 = [4, 9, y, 6]
        res.append(to_dec(n1, 67) + to_dec(n2, x))

print(len(set(res)))'''
'''
from itertools import permutations

num = '12345'
res = 0
for x in permutations('01234567', 5):
    x = ''.join(x)
    cnt = 0
    for i in range(5):
        if x[i] == num[i]:
            cnt += 1
    if cnt == 2:
        cnt = 0
        for i in x:
            if i in num:
                if x.index(i) != num.index(i):
                    cnt += 1      
        if cnt >= 2:
            res += 1

print(res)'''

def f(start, end, a):
    if start >= end:
        return start == end and any(sum(a[i:i+3]) % 11 == 0 for i in range(len(a) - 2))
    if start < end:
        return f(start + 2, 600, a + [start+2]) + f(start * 3, 600, a + [start*3]) + f(start * 4, 600, a + [start*4])

print(f(1, 600, [1]))