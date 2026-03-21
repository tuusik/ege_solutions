'''
for n in range(1001):
    N = n
    a = ''
    while N > 0:
        a = str(N%7)+a
        N = N//7
    if n%2 == 0:
        N = '52' + a + '1'
    else:
        N = a[-1] + a[1:-1] + a[0] +'15'
    N = N.lstrip('0')
    if n <= 1000 and len(N) == 4:
        print(n)
'''
'''
from turtle import *

tracer(0)
k = 20

for i in range(2):
    down()
for i in range(2):
    forward(8*k)
    right(90)
    forward(8*k)
    right(90)
up()
forward(6*k)
right(90)
forward(6*k)
left(90)
right(180)
forward(4*k)
down()
for i in range(4):
    forward(8*k)
    right(270)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(5, 'red')
done()
'''

'''
from itertools import product

K = 0
for i in product('012345678', repeat = 7):
    a = ''.join(i)
    if any(a[j]==a[j+1]==a[j+2] for j in range(5)):
        continue
    if a[0] == '0':
        continue
    if a[-1] == '3' or a[-1] == '4' or a[-1] == '7':
        continue
    else:
        K += 1
print(a, K)
'''
'''
rez = []
for i in range(96):
    n = i
    a = ''
    while n > 0:
        a = str(n%3) + a
        n //= 3
    n = i
    b = ''
    while n > 0:
        b = str(n%5) + b
        n //= 5
    
    if len(a) >= 2 and a[-2:] == '21' and b[0] == '3':
        rez.append(i)
print(sum(rez))
'''
'''
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)-2*g(n-1)

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)+2*g(n-1)

print(g(21))
'''