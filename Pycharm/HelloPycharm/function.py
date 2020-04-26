def add(a,b):
    sum = a + b
    return sum
print(add(1,2))

def add2(a,b):
    print(a + b)
add2(1,2)


#가변인자: 함수의 매개변수가 가변적일 수 있을 때 사용.
def function(*data):
    print(data)
function(1,2,3)


#지역변수와 전역변수
a = 10  #전역변수
print(a)

def add(a):  #지역변수
    a += 5

a = 2
add(a)
print(a)  #2 -> 전역변수

def add5():
    global a
    a += 5
a = 2
add5()
print(a)  #7


#파이썬의 함수는 반환값이 여러 개일 수 있음. -> tuple 형태로 반환
def funnction():
    a = 5
    b = [1,2,3]
    return a, b

a, b = funnction()
print(a)
print(b)

