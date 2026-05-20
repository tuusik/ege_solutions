'''def a(n):
    s = ''
    while n != 0:
        s = str(n % 5) + s
        n //= 5
    return s

def f(n):
    s = a(n)
    if len(s) % 2 == 0:
        s = s[len(s) // 2:] + s[:len(s) // 2]
    else:
        s = s + str(n % 5)
        s = s[len(s) // 2:] + s[:len(s) // 2]
    return int(s,5)

for i in range(1,1000):
    if f(i)>50:
        print(i)
        break'''

'''from turtle import*
k=20
speed(0)
tracer(0)
for i in range(15):
    forward(3*k)
    right(40)
up()
for x in range(-25, 25):
    for y in range(-25, 25):
        goto(x*k, y*k -180)
        dot(5,'red')
update'''

'''from itertools import*
c=0
m=0
for i in product(sorted('СДАЙЕГЭ'), repeat=6):
    b=''.join(i)
    c+=1
    if'ЕГЭ' in b:
        m+=c
print(m)'''

'''for x in range(0, 36):
    s=(1+3*37+x*37**2+8*37**3+9*37**4)+(4+2*37+9*37**2+x*37**3+1*37**4)
    if s%21==0:
        print(s//21)'''
'''a=[int(x)for x in open('17_14260.txt')]
t=[]
m=min(x for x in a if x>0 and 1000<= x <10000 and str(x)[-1]==str(x)[-2])
for i in range(len(a)-2):
    if all(100<=abs(x)<1000 for x in a[i:i+3]) > m:
        t.append(sum(a[i:i+3]))
print(len(t), max(t))'''

'''print('x y w z f')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x <= y)and(z or w))<=((x == w)or y and (not z)):
                    f=1
                else:
                    f = 0
                print(x, y, w, z, f)
x y w z f
0 0 1 0 0
0 0 1 1 0
0 1 1 1 0
1 1 0 1 0
1.y
2.x
3.w
4.z
5.f'''

'''def f(x, y, chislo):
    if x == y:
        return 1
    elif x < y or x == chislo:
        return 0
    else:
        return (f(x - 1, y, chislo) + f(x - 3, y, chislo) +
                f(x // 3, y, chislo))'''


