s = input()
cnt = 0
a = set()
for c in s:
    if c not in a:
        cnt += 1
        a.add(c)
print("CHAT WITH HER!" if cnt % 2 == 0 else "IGNORE HIM!")