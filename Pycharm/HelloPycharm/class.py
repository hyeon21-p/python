#클래스(class): 반복되는 불필요한 소스코드를 최소하 하면서
#              현실 셰계의 사물을 컴퓨터 프로그래밍 상에서
#              쉽게 표현할 수 있도록 해주는 프로그래밍 기술
#인스턴스: 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

# 클래스의 멤버: 클래스 내부에 포함되는 변수
# 클래스의 함수: 클래스 내부에 포함되는 함수. 메소드

class Car:
    # 클래스의 생성자. 항상 함수 형태로 존재
    def __init__(self, name, color):  #생성자 형태는 정해져있다.
        self.name = name #클래스의 멤버
        self.color = color

    #클래스 소멸자
    def __del__(self):
        print("인스턴스를 소멸시킵니다.")

    #클래스의 메소드
    def show_info(self):
        print("이름:", self.name, "/ 색상:", self.color)

    #Setter 메소드: 특정한 속성의 값을 변경할 때 사용
    def set_name(self, name):
        self.name = name

car1 = Car("소나타", "빨간색")  #메모리 상에 동적으로 할당
car1.show_info()
print(car1.name, "을(를) 구매했습니다!")
car1.set_name("마세라티")
car1.show_info()
del car1  #사용이 끝난 객체는 메모리 상에서 할당 해제
#car1.show_info() -> 오류 발생

car2 = Car("아반떼", "검은색")
car2.show_info()