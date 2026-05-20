'''print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))):
                                                         f = 1
                else:
                    f = 0
                print(w, x, y, z, f)
w x y z f
0 0 1 0 1
0 0 1 1 1
0 1 1 1 1

xwzy'''
'''
print(5+3+1+3+5+4+5)'''

'''from turtle import*
k = 20
speed(0)
tracer(0)
for i in range(2):
    forward(1*k)
    left(270)
    forward(16*k)
    right(90)
up()
back(4*k)
right(90)
forward(10*k)
left(90)
down()
for i in range(2):
    forward(17*k)
    right(90)
    forward(7*k)
    right(90)
up()
for x in range(10):
    for y in range(-10,30):
        goto (x*k, y*k - 180)
        dot(5, 'red')'''
'''from sys import setrecursionlimit
setrecursionlimit(10**6)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)
print((f(2024)-2*f(2023))/f(2022))'''

'''from itertools import*
k = 0
for x in product(('0123456'), repeat = 5):
    s=''.join(x)
    k= k+1
    if s.count('0')==1 and s.count('1') <= 2:
        print(k,s)'''

'''def f(x):
    P= x <= 21
    Q= x <= 77
    A=a1<=x<=a2
    return( P <= (not A)<=(not Q))
rez = []
dx =[y for x in(21, 77) for y in (x, x+0,1, x-0,1)]
for i in dx:
    if a2>a1 and all(f(x)==1 for x in dx):
        rez.append(a2-a1)
    print(min/max(rez))'''

for N in range(1, 1000):
    s = bin(N)[2:]
    if N%2 == 0:
        res= '10'+s
    else:
        res= '1'+s+'01'
    R = int(res, 2)
    if R>18:
        print(R)
    break
        
    

