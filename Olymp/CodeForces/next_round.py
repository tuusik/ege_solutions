n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] > 0:
        if i < k - 1:
            cnt += 1
        elif i == k - 1:
            t = a[i]
            cnt += 1
        elif a[i] == t:
            cnt += 1
print(cnt)