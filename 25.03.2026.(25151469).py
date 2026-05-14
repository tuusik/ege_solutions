#16
"""from sys import*
setrecursionlimit(100000)
def f(n):
    if n<110:
        return n
    if n>=110:
        return (n-7)*f(n-8)
print((f(74914) - f(74898)) / (16*f(74890)))"""

#15
"""def f(x,y):
    a1 = ((2*x + 3*y) != 150)
    a2 = (x<A)
    a3 = (y<A)
    return a1 or a2 and a3
for A in range(1000):
    if all(f(x,y)==1 for x in range(1,1000) for y in range(1,1000)):
        print(A)
        break"""
#14
"""from string import*
k=0
for x in printable[:16]:
    s = int(f"11{x}73",16) + int(f"94662{x}53{x}",16) + int(F"6{x}41",16) + int(f"31{x}77",16) + int(f"9{x}82{x}{x}181",16)
    if  s%15 == 0:
        k = s/15
        break
print(k)"""

#2
"""print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(((y or z)<=x) or (x == z)):
                f = 1
            else:
                f = 0
            print(x, y, z, f)
"""
"""
x y z f

0 0 1 0
0 1 1 0
"""
#8

"""
from itertools import*
k = 0
for x in product(sorted("ПРОСТО"), repeat = 6):
    a="".join(x)
    if a[:1] != a[1:2] and a[1:2] != a[2:3] and a[2:3] != a[3:4] and a[3:4] != a[4:5] and a[4:5] != a[5:6]:
        k += 1
print(k)
"""


