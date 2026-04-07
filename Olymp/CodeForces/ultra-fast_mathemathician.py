n1, n2 = input(), input()
print(bin(int(n1, 2) ^ int(n2, 2))[2:].zfill(len(n1)))