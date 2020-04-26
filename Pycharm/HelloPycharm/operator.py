#증감 연산자
a = 10
a = a + 10
print(a)
a += 10
print(a)

#관계 연산자
a = 3
b = 7
print(a == b)
print(a != b)
print(a > b)

#문자열도 비교 가능
a = "ABC"
b = "DEF"
print(a == b)
print(a < b)  #True -> 문자열 비교시 사전 순으로 비교.

#논리 연산자
a = True
b = False
print(a and b)
print(a or b)
print(not a)

if 3 > 5 or 7 < 10:
    print("야호!")
