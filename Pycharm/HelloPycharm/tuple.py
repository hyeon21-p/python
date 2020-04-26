tuple = (1,2,3)
for i in tuple:
    print(i)

list1 = [1,2,3]
list2 = [4,5,6]
tuple = (list1, list2)
print(tuple)
#tuple[0] = [7,8,9] -> 오류! 튜플은 변경 불가
tuple[0][0] = 7
print(tuple)

#인덱싱, 슬라이싱 등의 문법 사용 가능
tuple = (1,2,3,4,5,6,7,8,9)
print(tuple[0:5])
print(tuple[0:3] * 3)