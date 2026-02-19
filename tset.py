"""
f = open("17.txt")
a = [int(line) for line in f]
cnt = 0
max_kaka = 0
for i in range(int(line)-3):
    first, second = a[1] a[i+1]
    if

"""
cnt = 0
max_kaka = 0
f = open("17.01.txt")
a = [int(i)for i in f]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]* a[j]%14!=0:
            cnt+=1
            max_kaka = max(max_kaka, a[i] + a[j])
print(cnt)
print(max_kaka)
