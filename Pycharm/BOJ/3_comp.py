#세 정수 입력
num = input().split(" ")
num = list(map(int, num))  #문자열을 정수로 변환

num.sort()
print(num[1])