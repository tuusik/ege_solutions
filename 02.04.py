'''
print('w x y z F')

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not x and y and z and (not w)) or (not x and y and (not z) and (not w)) or (x and y and z and (not w)):
                    F = 1
                else: F = 0
                print(w, x, y, z, F)

w x y z F
0 0 1 0 1
0 0 1 1 1
0 1 1 1 1
x w z y
'''
rez = []
for N in range(1, 10000):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = '10' + n
    if N % 2 != 0:
        n = '1' + n + '01'
    R = int(n, 2)
    rez.append(R)
if N > 18:
    print(min(rez))