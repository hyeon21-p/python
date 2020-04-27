# 람다식 : 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법
# map() : 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있도록 도와줌

add = lambda x, y: x +y  #매개변수 지정하고 결과 설정
print(add(1, 2))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
my_funcion = lambda a, b: a * b
result = map(my_funcion, list1, list2)  #어떠한 함수를 리스트의 각 원소에 적용할 때 사용
print(result)  #map object 출력
print(list(result))  #list 형태로 출력