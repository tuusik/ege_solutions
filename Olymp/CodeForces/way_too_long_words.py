n = int(input())
for _ in range(n):
    w = input()
    print(w[0] + str(len(w) - 2) + w[-1] if len(w) > 10 else w)