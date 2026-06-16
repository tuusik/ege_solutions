'''s = [list(map(int, line.split())) for line in open('9_18258.txt')]

cnt = 1
res = 1


def cnt_dig(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

for line in s:
    if line == sorted(line):
        rep = [num if line.count(num) > 1 and cnt_dig(num) % 2 == 0 else 0 for num in line]
        if sum(rep) > 0:
            res = max(res, cnt)
    cnt += 1

print(res)'''
'''from string import printable
def to_dec(n, ns):
    res = 0
    power = 0
    for i in range(1, len(n) + 1):
        res += n[-i] * (ns ** power)
        power += 1
    return res

def to_thirteen(n):
    s = ''
    while n > 0:
        s = printable[n % 13] + s
        n //= 13
    return s

for x in range(2, 100):
    n = to_dec([3, x, 1, 5, x], 15) + to_dec([1, 2, 3], int(f"3{x}51")) + x**x + to_dec([1, x, 3], int(f"1{x}3")) + to_dec([1, x, 2], x + 1)
    if n % 13 == 0:
        print(x, to_thirteen(n))'''

'''def cnt_dig_even(n):
    cnt = 0
    while n > 0:
        if (n % 10) % 2 == 0:
            cnt += 1
        n //= 10
    return cnt

def cnt_dig_odd(n):
    cnt = 0
    while n > 0:
        if (n % 10) % 2 != 0:
            cnt += 1
        n //= 10
    return cnt

s = [int(num) for num in open('17_7717.txt')]

max_num = max([num for num in s if cnt_dig_even(num) == cnt_dig_odd(num)])
cnt = 0
max_sum = 0

for i in range(len(s) - 1):
    flag = True
    first, second = str(s[i]), str(s[i+1])
    for _ in range(len(str(s[i]))):
        if first < second:
            flag = False
            break
        first, second = first[1:], second[1:]
    if flag == True and s[i] + s[i+1] <= max_num:
        cnt += 1
        max_sum = max(max_sum, s[i] + s[i+1])

print(cnt, max_sum)'''
#66 а не 11 почему

'''def game(first, second, n):
    if first + second == 13 or n > 4:
        return n == 4
    
    actions = [game(first + 1, second, n + 1),
               game(first + 2, second, n + 1),
               game(first, second + 1, n + 1),
               game(first, second + 2, n + 1)]
    
    if n % 2 == 0:
        return all(actions)
    return any(actions)

for s in range(1, 10):
    if game(3, s, 0):
        print(s)'''

'''def f(x, A):
    p1 = x % 22229 == 0
    p2 = not(x % A == 0)
    p3 = not(x % 22247 == 0)
    return p1 <= (p2 <= p3)

for A in range(1, 100_000):
    if all(f(x, A) for x in range(1, 100_000)):
        print(A)
#кодом не решить, надо думать'''

from itertools import product

cnt = 0

for i in range(3, 6):
    for x in product('КРЫША', repeat = i):
        x = ''.join(x)
        if (x.count('Ы') <= 2 and x.count('А') <= 2) and ((x[0] in 'КРШ' and x.count('К') + x.count('Р') + x.count('Ш') == 1) or (x.count('К') + x.count('Р') + x.count('Ш') == 0)):
            print(x)
            cnt += 1
print(cnt)
