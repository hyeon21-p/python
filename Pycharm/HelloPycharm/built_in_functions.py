# input() : 사용자로부터 콘솔로 입력을 받는 함수. 문자열로 처리
# int() : 정수 자료형으로 변환
# float() : 문자열, 정수 등의 자료형을 실수형으로 변환
# max(), min() : 시퀀스 자료형에 포함되어 있는 원소 중 최대값 혹은 최소값을 구하는 함수
# bin(), hex() : 10진수 -> 2진수 변환, 10진수 -> 16진수 변환. 반환값은 문자열!!
# round() : 반올림을 수행
# type() : 자료형의 종류

user_input = input('정수를 입력하세요:')
print("세제곱:", int(user_input) ** 3)  #3제곱 출력! -> ** (제곱수)

a = "12345"
print(int(a))
print(float(a))  #문자열을 실수형으로 바꿈.
b = 12.5
print(int(b))  #실수형을 정수형으로 바꿈.

list = [3,6,9,5,2,8]
print(max(list))
print(min(list))

print(bin(128))  #0b10000000
print(hex(230))  #0xe6

print(int('0xe6', 16))  #230 -> 16진수를 10진수로 변환

print(round(123.756, 2))  #반올림해서 소수점 아래 두번째 자리까지 출력
print(round(123.756, -1)) #- 붙이면 소수점 위의 수까지 반올림 -> 120.0 출력

int = 1
str = "문자열"
list = [1,2,3]
dict = {'apple': '사과'}
print(type(int))
print(type(str))
print(type(list))
print(type(dict))