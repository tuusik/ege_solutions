'''
#2
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (x and (not y)) or (y==z) or w:
                    f = 1
                else:
                    f = 0
                print(x, y, w, z, f)


x y w z f
0 0 0 1 0
0 1 0 0 0
1 1 0 0 0

#6
from turtle import *

k = 20
tracer(0)
for i in range(2):
    forward(7*k)
    right(90)
    forward(18*k)
    right(90)
up()
backward(-2*k)
right(90)
forward(9*k)
left(90)
down()
for i in range(2):
    forward(8*k)
    right(90)
    forward(5*k)
    right(90)

up()

for x in range(10):
    for y in range(10):
        goto(x*k, y*k - 180)
        dot(5, 'red')
update()
#12
from ipaddress import*

from ipaddress import *
k = 0
network = ip_network(f'171.128.0.0/255.128.0.0')
for ip in network:
    if f'{ip:b}'[:16].count('1') < f'{ip:b}'[16:].count('1'):
        k += 1
print(k)'''
#16
from sys import setrecursionlimit
setrecursionlimit(10**6)
def f(n):
    if n < 7:
        return 7
    if n % 3 == 0:
        return 3 + f(n - 1)
    if n % 3 != 0:
        return 5 - f(n - 1)
print(f(3015))

