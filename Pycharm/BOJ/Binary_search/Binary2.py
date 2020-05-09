#BOJ 10816
N = int(input())
N_list = list(map(int, input().split(" ")))

M = int(input())
M_list = list(map(int, input().split(" ")))

for i in M_list:
    count = 0
    for j in N_list:
        if i == j:
            count += 1
    print(count, end = ' ')  #출력할 때 end에 원하는 문자를 넣어주면 줄바꿈 대신 원하는 문자 출력