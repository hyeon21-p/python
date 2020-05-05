N = int(input())  #회의의 수
list1 = []
list2 = []

for i in range(0, N):
    a = input().split(" ")
    list1.append(int(a[0]))
    list2.append(int(a[1]))

I = (list1, list2)
print(I)