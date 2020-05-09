#BOJ 1931
N = int(input())  #회의의 수
#N = sys.stdin.readline().rstrip('\n')
time = []

for i in range(0, N):
    a = input().split(" ")
    time.append((int(a[0]), int(a[1])))

time.sort()
#print(time[2][0]): 이차원 배열로 이용 가능

new_end = time[0][1]
count = 0
for i in range(1, N):
    if time[i][0] >= new_end:
        new_end = time[i][0]
        count += 1
    else:
        continue

print(count)