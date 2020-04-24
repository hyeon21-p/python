# -*- Encoding: utf-8 -*-
#리스트
a = [3.5, 4.3, 2.3, 3.8, 4.5, 3.3]
#print(a)  #[3.5, 4.3, 2.3, 3.8, 4.5, 3.3]
#print("인덱스 3 =", a[3]) #3.8

#print("인덱스 0 =", a[0])
a[0] = 0.9
#print("인덱스 0 =", a[0])  #0.9

#반복문
sum = 0
for i in a:  #i는 index로 a 안에 있는 값 가르킬 수 있음.
    sum = sum + i
#print("평균 점수: ", sum / len(a))  #len(a): a 배열의 길이를 구하는 함수

#이차원 배열
a = [
    [90, 95, 80, 30, 56, 87],
    [89, 86, 90, 99, 93, 76]
]
#print(a[0][3])
english = a[0]
for i in english:
    sum = sum + i
print("영어 점수의 평균:", sum / len(english))

sum = 0
math = a[1]
for i in math:
    sum = sum + i
print("수학 점수의 평균:", sum / len(math))