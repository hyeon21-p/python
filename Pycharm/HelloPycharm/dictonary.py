# 사전(Dictionary): 키(Key)와 값(Value) 한 쌍을 원소로 가지는 자료형

dict = {}  #사전 자료형은 {}이용
dict['안녕'] = 'Hello'  #dict[key 값] = value 값
dict['기적'] = 'Miracle'
dict['노력'] = 'effort'
print(dict)

# 키 값을 이용하여 값에 접근
for i, k in enumerate(dict):  #enumerate(): 각각의 데이터에 차례대로 접근할 수 있도록 바꿔줌.
    print("[인덱스:", i, "] 한글:", k, "/ 영어:", dict[k])

'''dict['안녕'] = 'Hi'  #어떠한 데이터가 특정한 자료구조에 포함되어 있는지 아닌지 확인할 때 편리함.
del dict['기적']
print(dict)

dict.clear()  #사전 자료형 다 지우는 내장함수
print("사전 자료형의 길이:", len(dict))'''

#키와 값만 따로 빼서 출력
keys = dict.keys()
print("키:", keys)  #dict.keys라는 자료형 가짐
keys_list = list(keys)  #리스트 형태로 바꿈
print("키 리스트:", keys_list)

values = dict.values()
value_list = list(values)
print("값 리스트:", value_list)

#특정한 키의 존재 여부 확인
if '안녕' in dict:
    print("[안녕] 키가 존재합니다.")

#정렬
scores = {}
scores['박진영'] = 90
scores['왕잭슨'] = 87
scores['정재현'] = 63
scores['이마크'] = 93
print(sorted(scores))  #키로 정렬하기 -> 기본적으로 오름차순으로 정렬
print(sorted(scores, reverse=True))  #키로 내림차순 정렬하기
print(sorted(scores.values()))  #값을 정렬하기