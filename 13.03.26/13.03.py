'''res = []

def f(start, cnt = 0):
    if cnt != 4:
        return f(start + 2, cnt + 1) + f(start * 3, cnt + 1)
    if cnt == 4:
        res.append(start)
        return 1
f(1)

print(len(set(res)))
'''

'''def game(first, n, prev):
    if first >= 62 or n > 4:
        return n == 2
    
    actions = [game(first + 1, n + 1, 0),
               game(first + 2, n + 1, 1),
               game(first * 3, n + 1, 2)]
    if n != 0:
        actions.pop(prev)
    if n % 2 == 0:
        return all(actions)
    return any(actions)

for i in range(1, 62):
    if game(i, 0, 0):
        print(i)'''

'''f = open('17_2011.txt')
s = [int(line) for line in f]
cnt = 0
max_num = 0
for i in range(0, len(s)):
    if str(s[i]).count('0') >= 2 and s[i] % 7 == 0:
        cnt += 1
        max_num = max(s[i], max_num)
print(max_num, cnt)
'''

'''from sys import setrecursionlimit
setrecursionlimit(100000)

def f(n):
    if n >= 10_000:
        return n
    if n < 10_000 and n % 6 == 0:
        return n // 6 + f(n // 6 + 2)
    if n < 10_000 and n % 6 != 0:
        return n + f(n + 2)

print(f(264) - f(7))'''

'''for x in range(1, 10000):
    n = 27**7 - 3**11 + 36 - x
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    if (s.count('1') + (s.count('2') * 2)) == 22:
        print(x)
        break'''

for n in range(1001, 1473):
    r = bin(n)[2:]
    print(r)
    r = r[::-1]
    print(r)
    r = r[r.index('1'):]
    print(r)
    if int(r, 2) == 29:
        print(n)
        break