#16.
'''from sys import setrecursionlimit
setrecursionlimit(10000)
def f(n):
    if n<7:
        return 7
    if n>=7 and n%3!=0:
        return 5 - f(n-1)
    if n>=7 and n%3==0:
        return 3 + f(n-1)
print(f(3015))
'''
#15
"""
def f(x):
    return ((x%A == 0) and not(x%50 == 0)) <= (not(x%18 == 0) or (x%50 == 0))
for A in range(1,1000):
    if all(f(x)==1 for x in range(1,1000)):
        print(A)
        break
"""
#8

"""
from itertools import*
c = 0
for i in product(sorted("ШКОЛА"), repeat = 5):
    a = "".join(i)
    if a.count("А")>=1 or a.count("О")>=1:
        c +=1
print(c)
"""
#5
"""
import math
for i in range(2;10000):
    if 
    """
#14
for p in range(18, 30):
   n1 = int('22A12E', p)
   n2 = int('2F1391', p)
   n3 = int('1H05D0',p)
   s = n1 + n2 - n3
   if s % 19 == 0:
       print(s // 19)
       break

#23

