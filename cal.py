# -*- Encoding: utf-8 -*-
#내 코드
print("두 정수를 입력하세요.")
a = input()
b = input()

sum = int(a) + int(b)

print("두 정수의 합은", sum, "입니다.")


#입력값이 3 7인 경우
a = input().split(" ")

#a = ['3', '7']
x = int(a[0])
y = int(a[1])

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)