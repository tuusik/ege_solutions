'''def game(s, n, flag):
    if s >= 20 or n > 10:
        return n == 4 or n == 2 or n == 6 or n == 8 or n == 10
    actions1 = [game(s * 2, n + 1, flag),
                game(s + 2, n + 1, flag),
                game(s, n + 1, True)]
    actions2 = [game(s * 2, n + 1, flag),
                game(s + 2, n + 1, flag)]
    if n % 2 == 0:
        if flag == False:
            return all(actions1)
        return all(actions2)
    if flag == False:
        return any(actions1)
    return any(actions2)

for s in range(1, 20):
    if game(s, 0, False):
        print(s)'''

'''def f(start, end, flag):
    if start == 4 or start == 16:
        if flag == True:
            return 0
        flag = True
    if start == end:
        return 1
    if start > end:
        return 0
    if start < end:
        return f(start * 2, end, flag) + f(start ** 2, end, flag) + f(start ** 3, end, flag)
    
print(f(2, 131072, False))'''

'''from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return f(n - 1) - 2 * g(n - 1)

@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    return f(n - 1) + g(n - 1) + n

for n in range(1, 37):
    f(n)
    g(n)

print(g(36))'''

'''from itertools import product

cnt = 0

for i, x in enumerate(product(sorted('УЖЕМАЙ'), repeat= 5), 1):
    x = ''.join(x)
    if i % 2 == 0 and 'УУ' not in x and 'ЖЖ' not in x and 'ЕЕ' not in x and 'ММ' not in x and 'АА' not in x and 'ЙЙ' not in x:
        cnt += 1
print(cnt)'''

a = [int(num) for num in open('17_2011.txt')]

cnt = 0
max_num = 0

for num in a:
    if str(num).count('0') >= 2 and num % 7 == 0:
        cnt += 1
        max_num = max(max_num, num)
print(max_num, cnt)