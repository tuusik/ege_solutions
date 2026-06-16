from sys import stdin

s = ''.join(map(lambda x : x[:-1:2], stdin.readlines()))

for i in range(len(s)):
    if s[i] == '1':
        print(abs(i % 5 - 2) + abs(i // 5 - 2))
        break