# 문자열 자료형 뒤집기 : 슬라이싱 활용
# len() : 문자열의 길이를 출력
# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인
# isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
# isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
# join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수
# sorted(문자열 자료형) : 각 문자를 정렬하는 함수
# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수. 결과를 리스트에 담는다.
# find(서브 문자열) : 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
# upper(). lower() : 문자열을 대문자로 혹은 소문자로 변환해주는 함수
# strip() : 좌우로 특정한 문자열을 제거하는 함수
# eval() : 문자열 수식 계산해주는 함수

str = "Hello World"
print(str[::-1])  #str[시작:끝:-1(반대로)]
print(len(str))  #문자열 자료형은 시퀀스 자료형에 속함. len()와 같은 다양한 함수 사용 가능
print(str.isalpha())  #False -> 공백 존재

str2 = "sneaky교활한"
print(str2.isalpha())  #True -> 아스키코드로 판별하기 때문에 한글도 가능

str = "123123"
print(str.isdigit())

str = "abc#123"
print(str.isalnum())

list = ['MarkLee', '너무', '귀여워']
print(' '.join(list))  #한 칸 띄어쓰기를 구분자로 쓰면서 list의 원소 합쳐서 하나의 문자열로

str = "helloworld"
list = sorted(str)  #오름차순으로 정렬 -> list 자료형이 됨!
print(list)
print(''.join(list))
list = sorted(str, reverse=True) #내림차순 정렬
print(list)

str = "I wanna go Got7 concert and NCT concert."
list = str.split(' ')
print(list)
print(str.find('concert', 17))  #16 -> concert의 c의 인덱스를 반환
#특정 문자열이 두개 존재할 경우 -> 17이상의 인덱스에서 문자열 찾아라.
print(str.find('nct'))  #-1 반환 -> 특정 문자열이 포함되어 있지 않을 때(대소문자 구별)

print(str.upper())
print(str.lower())

str = " Hello World "
print(str.strip())  #디폴트 값이 공백을 제거
print(str.lstrip())  #왼쪽의 공백만 제거
print(str.rstrip())  #오른쪽의 공백만 제거

str = "ttHello Worldtt"
print(str.strip('t'))

exp = "(203+705)*3-(30/6)"
print(eval(exp))  #문자열 형태로 이루어진 특정한 계산식을 계산해준다.