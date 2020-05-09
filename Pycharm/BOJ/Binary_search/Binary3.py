#BOJ 8653
a = input().split(" ")
K = int(a[0])
N = int(a[1])
lan = []

for i in range(0, K):
    lan.append(int(input()))

lan.sort()
k = K - 1
for i in range(lan[k], 0, -1):  #1씩 감소시킴
    count = 0
    for j in lan:
        result = j // i
        count += result
    if count >= N:
        print(i)
        break