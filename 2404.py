'''print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not y)<=(z==w) and (z<=x)==w):
                    f = 1
                else:
                    f = 0
                print(x, y, z, w, f)
x y z w f
0 1 0 1 1
0 1 1 0 1
1 0 1 1 1
1 1 0 1 1
1 1 1 1 1'''

'''for N in range(1, 1000):
    S = bin(N)[2:]
    if N % 5 == 0:
        res = S + '01'
    else:
        res = S + '10'
    R = int(res, 2)
    if R > 370:
        print(R)
        break'''

'''from turtle import *
t = turtle.Turtle()

k = 20
speed(0)
tracer(0)
for i in range(27):
    forward(k*5)
    t.fillcolor('red')
    backward(k*3)
    t.fillcolor('blue')
    backward(k*3)

for x in range(1, 100):
    for y in range(1, 100):
        goto(x*k, y*k):
        dot(5, 'green')
update()'''

'''for n in range(1, 1000):
    base6 = ""
    temp = n
    while temp > 0:
        base6 = str(temp % 6) + base6
        temp //= 6
    base5 = ""
    temp = n
    while temp > 0:
        base5 = str(temp % 5) + base5
        temp //= 5
    if len(base6) == 2 and len(base5) == 3 and n % 11 == 1:
        print(n)'''
'''from sys import setrecursionlimit
setrecursionlimit(10000)
def g(n):
    def f(n):
        if n > 1:
            return 1
        if  n > 1:
            return f(n-1)-2*g(n-1)
        if n > 1:
            return f(n-1)+g(n-1)
print(g(36))'''

def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        return f(x * 2, y) + f(x ** 2, y) + f(x ** 3, y)
ans1 = f(2, 131072)
ans2 = f(2, 4) * f(4, 16) * f(16, 131072)
print(ans1 - ans2)


