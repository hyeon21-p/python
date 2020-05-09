#BOJ 11399
N = int(input())
time = input().split(" ")
time = list(map(int, time))

time.sort()

tot = 0
for i in range(0, N):
    sum = 0
    for j in range(0, i+1):  #범위의 끝은 실제 인덱스+1
        sum += time[j]
    tot += sum

print(tot)