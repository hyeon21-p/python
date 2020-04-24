#-*- Encoding: utf-8 -*-
score = 75
if score >= 80:  #조건식(연산식)
    print("Good")  #들여쓰기
    print("점수가 80점을 넘었습니다.")    
elif score >= 70:
    print("Not Bad")  #들여쓰기
    print("점수가 70점을 이상입니다.")    
else:
    print("Bad")
    
print("어떤 내용")  #들여쓰기가 없기 때문에 조건에 상관없이 실행

if score < 90 and score >= 80:  #연산자가 하나씩만 들어가게!
    print("Good")
elif score < 80 or score >= 90:  #and, or 이용
    print("Not Bad")
    
#list에서 조건문을 이용하여 원소 확인    
list = [1, 2, 3]
if 6 in list:
    print("2가 리스트에 포함되어있습니다.")