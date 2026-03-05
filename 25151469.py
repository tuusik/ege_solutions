#2

"""print("x y z f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((y or z)<=x) and (x == y):
                f = 1
            else:
                f = 0
            print(x, y, z, f)
"""


"""
x y z f

0 0 0 1
0 0 1 0
0 1 0 0
0 1 1 0
1 0 0 0
1 0 1 0
1 1 0 1
1 1 1 1
"""     

#5
def f(n):
    if R == 0:
        return 0
    x = ""
    while n>0:
        x = str(n%3) + x
        n = n//3
    return x
def f(R):
    if R == 0:
        return 0
    x = ""
    while R>0:
        x = str(R%3) + x
        R = R//3
    return x
for n in range(100000):
    y = f(n)
    if n%3==0:
        r = "1" + str(y) + '02'
    else:   
        R = ((n%3)*4)
        r = f(R)
    K = int(r,3)
    if K<100:
        G = n
print(G)
        
       