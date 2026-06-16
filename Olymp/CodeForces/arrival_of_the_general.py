n = int(input())
s = list(map(int, input().split()))

s_max = s.index(max(s))
s_min = n - s[::-1].index(min(s)) - 1

if s_max == 0 and s_min == n - 1:
    print(0)
elif s_max < s_min:
    print(s_max + n - s_min - 1)
else:
    print(s_max + n - s_min - 2)