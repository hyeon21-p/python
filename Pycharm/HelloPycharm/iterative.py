sum = 0
for i in range(1, 10):
    print(i)
    sum = sum + i
print("합계: ", sum)


count = 0
for i in "Hello World":
    print(i)
    if i == 'o':
        count = count + 1
print("o의 개수는", count, "개 입니다.")


sum = 0
list = [1,2,3,4,5]
for i in list:
    sum = sum + i
print("합계:", sum)


#continue: continue를 만났을 때 더 이상 명령어를 실행하지 않고 다음 반복을 진행
#break: break를 만났면 반복문 벗어남
sum = 0
list = [1,2,3,4,5]
for i in list:
    if i % 2 == 1:
        continue  #홀수일 때, sum + i 실행X
    elif i % 4 == 0:
        break  #4의 배수일 때, 반복문 종료
    sum = sum + i
print("짝수의 합:", sum)


#while문
i = 0
sum = 0
while i <= 5:
    i = i + 1
    if i % 2 == 1:
        continue
    sum = sum + i
print("짝수의 합:", sum)