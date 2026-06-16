'''from itertools import product

cnt = 0
for x in product('0123456789', repeat=6):
    x = ''.join(x)
    if '34' not in x and x.count('0') > 0:
        x = x.replace('2', '0')
        x = x.replace('3', '1')
        x = x.replace('4', '0')
        x = x.replace('5', '1')
        x = x.replace('6', '0')
        x = x.replace('7', '1')
        x = x.replace('8', '0')
        x = x.replace('9', '1')
        if '11' not in x and '00' not in x:
            cnt += 1
print(cnt)'''

'''from math import prod
s = [list(map(int, line.split())) for line in open('9_13824.txt')]
res = []
cnt = 1
for line in s:
    if all(line[i] % 2 != line[i+1] % 2 for i in range(len(line) - 1)):
        repeat = [num for num in line if line.count(num) > 1]
        not_repeat = [num for num in line if line.count(num) == 1]
        if sum(not_repeat) * 3 >= prod(repeat):
            res += [cnt]
    cnt += 1
print(sum(res))'''

def to_fifth(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s

res = []

for x in range(1, 1000):
    for y in range(1, 1000):
        n = to_fifth((55 + 2 * 5 ** x) * 5 ** x + 55 + 5 ** y)
        sum = n.count('1') + n.count('2') * 2 + n.count('3') * 3 + n.count('4') * 4
        res.append(sum)
        print(sum)
print(max(res))
#очень долго. дошел до 9 макс. что то тут не чисто