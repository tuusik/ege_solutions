'''def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end and start % 2 == 0:
        return f(start+1, end) + f(start+2, end) + f(start*2, end)
    if start < end and start % 2 != 0:
        return f(start*2, end)
    
print(f(1, 32))'''

'''s = [c for c in range(1, 21)]
p1 = [c for c in s if c + 1 >= 21 or c * 2 >= 21]
p2 = [c for c in s if c + 1 in p1 and c * 2 in p1]
p3 = [c for c in s if c + 1 in p2 or c * 2 in p2]
pMT = [c for c in s if copied its stolen]
p4 = [c for c in s if c + 1 in p1+p3 and c * 2 in p1+p3]
p5 = [c for c in s if c + 1 in p4 or c * 2 in p4]
print(p1, p2, p3, p4, p5, sep = '\n')'''

'''f = open('17_11236.txt')
s = [int(num) for num in f]

cnt = 0
min_double = min([num for num in s if len(str(abs(num))) == 2])
max_quad = max([num for num in s if len(str(abs(num))) == 4 and abs(num) % 10 == 1])
max_sum = -300_000 

for i in range(len(s) - 2):
    first, second, third = s[i], s[i+1], s[i+2]
    count_bool = sum([1 for num in s[i:i+3] if num > min_double**2])
    if count_bool == 2 and (abs(first) * abs(second) * abs(third)) % max_quad == 0:
        cnt += 1
        max_sum = max(max_sum, abs(first) + abs(second) + abs(third))

print(cnt, max_sum)'''

'''f = [-1 for _ in range(200)]
for n in range(-100, 100):
    if n <= 0:
        f[n] = n
    if n > 0 and n % 2 == 0:
        f[n] = f[n // 2] + 5 * n
    if n > 0 and n % 2 != 0:
        f[n] = f[n - 4] - f[n - 6]

print(f[70] + f[56] - f[66] - f[44])'''

'''for x in range(100000):
    n = 4**1014 - 2**x + 12 
    if bin(n)[2:].count('0') == 2000:
        print(x)'''

def nine(n):
    s = ''
    while n > 0:
        s = str(n % 9) + s
        n //= 9
    return s

cnt = 0
print(nine(81))
for x in range(1_000_000, 10_000_000):
    x = nine(x)
    if (int(x[0]) % 2 == 0) and (int(x[-1]) % 3 != 0) and (x.count('6') > 1):
        cnt += 1
print(cnt)