from itertools import*
k = 0
for x in permutations(sorted('КИДАЛА'), 5):
    s = ''.join(x)
    k = k + 1
    if s.count('АА')== 0:
        print(k,s)



def f(x):
    q = 25<=x<=120
    p = 1<=x<=40
    a = a1 <= x <= a2
    return q <= (not(p)and(q)<=a)
h = [y for x in (1, 25, 40, 120)for y in (x, x + 0.1, x - 0.1)]
rez = []
for a1 in h:
    for a2 in h:
        if a2 > a1 and all(f(x) == 1 for x in h):
        print(a2 - a1)





from sys import setrecursionlimit
setrecursionlimit(50000)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n%2 == 0:
        return f(n+2)-3
    if n < 10000 and n%2 != 0:
        return f(n+2) +1
print(f(94) - f(80))




f = open("17.txt")
a = [int(i) for i in f]
k = 0
sum_el_93 = 0
max_el_93 = max(i for i in a if i % 100 == 93)
for i in range(len(a) - 1):
    if ((a[i] > max_el_93) + (a[i + 1] > max_el_93)) == 1:
        if str(a[i])[0] == '9' or str(a[i + 1])[0] == '9':
            k += 1
            sum_el_93 += a[i] if a[i] > max_el_93 else a[i + 1]
print(k,sum_el_93)
