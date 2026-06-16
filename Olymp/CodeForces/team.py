n = int(input())
cnt = 0
for _ in range(n):
    t = map(int, input().split())
    cnt = cnt + 1 if sum(t) >= 2 else cnt
print(cnt)