f = open("17_23376.txt")

a = [int(line) for line in f]

cnt = 0
mem = 0
max_sum_kaka = max([num for num in a if abs(num%37)==0 and (100000>abs(num)>=10000)])
for i in range(len(a)-1):
    first, second = a[i], a[i+1]
    if (((100000>abs(first)>=10000) and not(100000>abs(second)>=10000)) or (not(abs(100000>(first)>=10000)) and (100000>abs(second)>=10000)))and (first+second)**2>((max_sum_kaka)**2):
        cnt += 1
        mem = max(mem, first + second)
print(cnt,mem)



"""
#          0    1    2    3    4 
test_a = ["a", "b", "c", "d", "e"]

#Рядом стоящие
for i in range(len(test_a)-1):
    print(i, test_a[i], i+1, test_a[i+1])

#Все возможные
for i in range(len(test_a)):
    for j in range(i+1, len(test_a)):
        print(i,j,test_a[i],test_a[j])
        """
