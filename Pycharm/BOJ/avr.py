import sys

c = int(input())  #테스트 케이스 개수

for k in range(0, c):
    std = sys.stdin.readline().rstrip('\n').split(" ")  #테스트 케이스
    std = list(map(int, std))
    #평균 구하기
    sum = 0
    for i in range(1, len(std)):
        sum = sum + std[i]
    avr = sum / std[0]
    #평균을 넘는 학생의 수
    count = 0
    for j in range(1, len(std)):
        if std[j] > avr:
            count += 1
    result = count / std[0] * 100 #round(count / std[0] * 100, 3)
    print(result)
    print("%.3f%c" %(result, '%'))  #소수점 아래 세자리수에서 반올림해서 출력
