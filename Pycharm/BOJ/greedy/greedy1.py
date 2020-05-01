x = input().split(" ")
N = int(x[0])  #동전의 종류
K = int(x[1])  #가치의 합
coin = []  #빈 리스트 생성
#coin = list()
count = 0

for i in range(0, N):
    coin.append(int(input()))  #리스트에 원소 추가
    #coin.insert(i, int(input()))

coin.sort(reverse=True)
for i in coin:
    if i > K:
        continue
    else:
        try:
            if K // i > 0:
                count = count + (K // i)
                K = K % i
            else:
                continue
        except:
            break

print(count)
