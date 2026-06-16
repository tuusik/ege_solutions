def solve():
    s = input()
    h = 'hello'
    l = 0
    for r in range(len(s)):
        if s[r] == h[l]:
            l += 1
        if l == 5:
            print("YES")
            return
    print("NO")
    return

solve()