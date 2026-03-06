from itertools import*
k = 0
for x in permutations(sorted('ПРОБНИК'), 7):
    s = ''.join(x)
    k = k + 1
    if x[0] not in ('ОИ') and x[6] not in 'ОИ' and s.count('ОИ') == 0 and s.count('ИО')== 0:
        print(k,s)



        
for x in range(0,32001):
    s = 75**314 + 75**118 - x
    s = str(s%75) + s
    x = x//75
    if x > 0 and x < 32001:
        print(x.count('0'))


def f(x):
    a1 = x%45 == 0
    a2 = x%15 == 0
    a3 = x%A == 0
    return (a1 and (not(a2)))<= (not(a3))
for A in range(1,1000):
    if all (f(x) == 1 for x in range(1,1000)):
        print(A)


def f(n):
    if n < 3:
        return 1
    if n > 2 and n %2 == 0:
        return f(n-1) + 2*n - 1
    if n > 2 and n % 2 != 0:
        return f(n-2) + 2*n
print(f(21) - f(19))



f = open('17_1994.txt')

a = [int(line) for line in f]
cnt = 0
for i in range(len(a) - 1):
    first, second = a[i], a[i + 1]
    if (first*second) > 0 and (first + second) % 7 == 0:
        cnt += 1
print(cnt, (first*second))



