# open() : 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w
# read() : 파일 객체로부터 모든 내용을 읽는 함수
# seek(바이트) : 지정한 바이트 이후부터 리소스 사용
# readline() : 파일 내 데이터를 한 줄 씩 문자열을 읽는 함수
# readlines() : 전체 내용을 한 번에 리스트에 담는 함수
# with : 파일 open, close, 메모리 할당 해제 자동으로!

#파일 객체 생성
f = open("input.txt", "r", encoding="UTF-8")  #한글이 포함될 경우, 인코딩 방식 넣어줘야함.

'''f.seek(9)  #9byte -> 한글은 3byte 차지
data = f.read()
print(data)
f.close()  #해당 파일에 대한 리소스 사용이 끝났다고 알려줌
'''

'''count = 0
while count < 3:
    data = f.readline()
    count = count + 1
    print("%d번째 줄: %s" %(count, data), end='')
f.close()'''

'''list = f.readlines()
print(list)  #마지막에 줄바꿈 기호 나옴.

for i, data in enumerate(list):
    print("%d번째 줄: %s" %(i + 1, data), end='')  #i는 인덱스이므로 +1 해줘야
f.close()'''

#with 나온 순간 자동으로 파일 객체의 메모리가 할당 해제 -> f.close 사용X
with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄: %s" %(i + 1, data), end = '')