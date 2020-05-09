#BOJ 52329
N = int(input())
A = list(map(int, input().split(" ")))

M = int(input())
B = list(map(int, input().split(" ")))

for i in B:
    for j in range(0, M):
        if i == A[j]:
            print(1)
            break
        elif j == len(A)-1:
            print(0)