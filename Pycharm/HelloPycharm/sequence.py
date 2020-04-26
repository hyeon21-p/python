string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(string[0])
print(list[0])
print(tuple[0])

print(string[0:5])
print(list[0:5])
print(tuple[0:5])

for i in string:
    print(i)

string1 = "Hello World"
string2 = ", Python"
print(string1 + string2)

#len: 길이 출력
print(len(string1 + string2))

#반복문 등에서 사용 가능
list = [1,2,3,4,5]
print(4 in list)  #True
if 3 in list:
    print("3을 포함하고 있습니다.")