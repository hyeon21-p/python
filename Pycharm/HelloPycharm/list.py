# index(원소) : 리스트 내 특정한 원소의 인덱스를 찾기
# reverse() : 리스트의 원소를 뒤집기
# sum(리스트 자료형) : 리스트의 모든 원소의 합
# range(시작, 끝) : 특정 범위(시작~(끝-1))를 지정
# list(특정 범위) : 특정 범위의 원소를 가지는 리스트를 반환 -> 변수명에 list가 존재하면 안됨.
# all() / any() : 리스트의 모든 원소가 참인지 판별 / 하나라도 참인지 판별
# enumerate() : 리스트에서 인덱스와 원소를 함께 추출
# sort() : 리스트의 원소를 정렬
# count() : 특정한 원소의 개수를 추출
# del : 리스트의 특정 원소를 제거
# insert(인덱스, 원소값) : 리스트에 특정 원소를 삽입
# append() : 리스트의 가장 마지막 원소로서 원소를 삽입

'''list = ['박진영', '왕잭슨', '정재현', '이마크', '런쥔']
print(list.index('이마크'))
#print(list.index('왕이보'))  #존재하지 않는 원소 -> 오류메세지

list.reverse()  #반환값이 없음 -> 뒤집은 후 print에 넣어야함.
print(list)
#list = list[::-1] -> 슬라이싱 이용 경우 반환값이 있음.
print(list[::-1])  #슬라이싱 이용 가능

list = [1, 2, 3, 0.75]
print(sum(list))

my_range = range(3, 9)
print(my_range)
my_list = list(my_range)
print(my_list)'''

bool_list = [True, False, True]
print(all(bool_list))  #False
print(any(bool_list))  #True

my_list = ['박진영', '왕잭슨', '정재현', '이마크', '런쥔']
result = list(enumerate(my_list))
print(result)  #튜플 형태로 반환

for i, k in enumerate(my_list):
    print("인덱스:", i, "/ 원소:", k)

my_list.sort()  #오름차순 정렬
print(my_list)
print(my_list.count('정재현'))

del my_list[1:3]
print(my_list)

my_list.clear()
print(my_list)

my_list.insert(3, '왕이보')
print(my_list)
print(my_list.index('왕이보'))  #0

my_list.append('샤오잔')
print(my_list)